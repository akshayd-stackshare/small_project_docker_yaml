from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ScrapeError(BaseModel):
    body: Optional[str]
    url: str
    err_type: str
    err_msg: str
    utc_time: datetime
