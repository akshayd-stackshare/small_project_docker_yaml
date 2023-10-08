from fastapi import FastAPI
import json

from data_infrastructure.rabbitmq.service import RabbitMQService
from system.models.input import ScrapeRequest

app = FastAPI()


@app.post("/scrape")
async def create_scrape_job(request: ScrapeRequest):
    print(f'Sending scrape job to queue, url:{request.url}!')

    test_request = json.dumps(request.model_dump(), default=str)
    print(test_request)
    print(type(test_request))
    rabbit_service = RabbitMQService()
    rabbit_service.publish('input_queue', test_request)

    return {"message": f"Scrape job for {request.url} has been added to the queue"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
