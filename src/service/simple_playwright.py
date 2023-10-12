import json
import pprint
import time
import traceback
from datetime import datetime


import settings
from metadata.transform.shared.convert import get_domain_from_fqdn
from rate_limiting.distributed.leaky_bucket import RedisLeakyBucket
from src.data_infrastructure.arangodb.shared.pydantic.write import write_pydantic_to_arangodb
from src.data_infrastructure.rabbitmq.service import RabbitMQService
from src.methods.playwright.simple import download_url
from src.system.models.errors import ScrapeError
from src.system.models.input import ScrapeRequest

scrape_request = None


def process_message(ch, method, properties, body):
    global scrape_request
    try:
        msg = json.loads(body)

        scrape_request = ScrapeRequest(**msg)
        print(scrape_request)

        write_pydantic_to_arangodb(scrape_request)
        domain = get_domain_from_fqdn(str(scrape_request.url))
        LEAKY_BUCKET = RedisLeakyBucket(redis_host=settings.REDIS_HOST,
                                        capacity=4,
                                        leak_rate=1,
                                        fqdn=domain)  # 10 requests capacity, and it leaks at 1 request per second
        while not LEAKY_BUCKET.can_consume():
            pprint.pprint(f'waiting for capacity for domain:{domain} && {scrape_request.url}')
            time.sleep(0.1)
        else:
            download_url(url=scrape_request.url, correlation_id=scrape_request.correlation_id)

    except Exception as e:
        traceback.print_exc()
        # capture unknown / unhandled exceptions for further review
        tb_str = traceback.format_exc()
        error_class_str = e.__class__.__name__

        se = ScrapeError(correlation_id=scrape_request.correlation_id,
                         body=body,
                         url=str(scrape_request.url),
                         err_type=error_class_str,
                         err_msg=tb_str,
                         utc_time=datetime.utcnow())

        write_pydantic_to_arangodb(se)


if __name__ == '__main__':

    # create an input object to test against
    data = {
        "url": "https://www.yahoo.com",
        "time_requested": str(datetime.utcnow().isoformat())
    }

    test_request = json.dumps(ScrapeRequest(**data).model_dump(), default=str)
    print(test_request)
    print(type(test_request))

    rabbit_service = RabbitMQService()
    rabbit_service.publish('input_queue', test_request)

    try:
        rabbit_service.consume_with_retry('input_queue', process_message)
    except KeyboardInterrupt:
        print("Stopping service...")
    finally:
        rabbit_service.close()
