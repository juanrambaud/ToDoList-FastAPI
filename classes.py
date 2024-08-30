from pydantic import BaseModel
from enum import Enum
from datetime import date, datetime


class Task(BaseModel):
    #id: None
    learn: str
    stage: str = "To Do"
    comment: str
    date: datetime = date.today()


class type_stage(str, Enum):
    ToDo = "To Do"
    Doing = "Doing"
    Done = "Done"
