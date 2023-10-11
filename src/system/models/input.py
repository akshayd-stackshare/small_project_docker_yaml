from uuid import uuid4, UUID

from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime


class ScrapeRequest(BaseModel):
    correlation_id: UUID = Field(default_factory=uuid4)
    url: HttpUrl
    time_requested: datetime


if __name__ == '__main__':
    data = {
        "url": "https://www.example.com",
        "time_requested": datetime.utcnow().isoformat()
    }

    request = ScrapeRequest(**data)
    print(request)
