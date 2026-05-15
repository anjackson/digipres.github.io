from pydantic import BaseModel, PositiveInt
from typing import Optional
import datetime

class Presentation(BaseModel):
    title: str
    organisation: str
    presenter: str
    slides: Optional[str] = None
    recording_url: Optional[str] = None
    workflows: Optional[list[str]] = None
    link: Optional[str] = None

class Webinar(BaseModel):
    title: str
    presentations: list[Presentation]
    date: datetime.date
    start: str
    end: str

class WebinarSeries(BaseModel):
    title: str
    type: str = 'workflow-webinar'
    webinars: list[Webinar]
    date: datetime.date
    start: datetime.date
    end: datetime.date
    body: Optional[str] = None
