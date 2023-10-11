from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ScrapeError(BaseModel):
    correlation_id: UUID
    body: Optional[str]
    url: str
    err_type: str
    err_msg: str
    utc_time: datetime
