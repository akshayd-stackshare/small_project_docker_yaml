from pydantic import BaseModel, HttpUrl
from datetime import datetime


class ScrapeRequest(BaseModel):
    url: str
    time_requested: datetime


if __name__ == '__main__':
    data = {
        "url": "https://www.example.com",
        "time_requested": datetime.utcnow().isoformat()
    }

    request = ScrapeRequest(**data)
    print(request)
