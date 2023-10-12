from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, HttpUrl


class URLMetadata(BaseModel):
    correlation_id: UUID
    url: HttpUrl
    screenshot_path: str
    har_path: str
    html_path: str
    utc_time: datetime
