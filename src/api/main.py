from fastapi import FastAPI
import json

import settings
from data_infrastructure.rabbitmq.service import RabbitMQService
from system.models.input import ScrapeRequest

app = FastAPI()


@app.post("/scrape")
async def create_scrape_job(request: ScrapeRequest):
    print(f'Sending scrape job to queue, url:{request.url}!')

    test_request = json.dumps(request.model_dump(), default=str)
    print(test_request)
    print(type(test_request))
    rabbit_service = RabbitMQService(host=settings.RABBIT_HOST)
    rabbit_service.publish('input_queue', test_request)

    return {"message": f"Scrape job for {request.url} has been added to the queue"}


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.API_PORT)


if __name__ == "__main__":
    main()
