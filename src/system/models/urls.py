from datetime import datetime

from pydantic import BaseModel


class URLMetadata(BaseModel):
    url: str
    screenshot_path: str
    har_path: str
    html_path: str
    utc_time: datetime
