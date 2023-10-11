import json
import time
import traceback
from datetime import datetime

from rate_limiting.local.leaky_bucket import LeakyBucket
from src.data_infrastructure.arangodb.shared.pydantic.write import write_pydantic_to_arangodb
from src.data_infrastructure.rabbitmq.service import RabbitMQService
from src.methods.playwright.simple import download_url
from src.system.models.errors import ScrapeError
from src.system.models.input import ScrapeRequest

LEAKY_BUCKET = LeakyBucket(10, 1)  # 10 requests capacity, and it leaks at 1 request per second
scrape_request = None


def process_message(ch, method, properties, body):
    global scrape_request
    try:
        msg = json.loads(body)

        scrape_request = ScrapeRequest(**msg)
        print(scrape_request)

        write_pydantic_to_arangodb(scrape_request)

        # todo: implement other rate limiting strategies
        # todo: modify ScrapeRequest data model to hold which strat to use
        # todo: a global limiter using redis perhaps.
        # todo: would require a service that manages a single RedisLeakyBucket instance
        # todo: would just need to save/load outputs from current rate limiting strategies
        # todo: would need to add an environment var to determine whether to use a
        #  service level limiter or a global limiter
        # todo: could get fancier and implement a limiter by website though.
        while not LEAKY_BUCKET.can_consume():
            time.sleep(0.1)
        else:
            download_url(url=scrape_request.url)

    except Exception as e:
        traceback.print_exc()
        # capture unknown / unhandled exceptions for further review
        tb_str = traceback.format_exc()
        error_class_str = e.__class__.__name__

        se = ScrapeError(correlation_id=scrape_request.correlation_id,
                         body=body,
                         url=scrape_request.url,
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
