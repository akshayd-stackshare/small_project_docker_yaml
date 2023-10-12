from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl


class ScrapeError(BaseModel):
    correlation_id: UUID
    body: Optional[str]
    url: HttpUrl
    err_type: str
    err_msg: str
    utc_time: datetime
