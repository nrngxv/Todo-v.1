#defining models for main.py
from pydantic import BaseModel
from enum import Enum

#enum simplyfies the class
class Category(Enum):
    WORK = "work"
    PERSONAL = "personal"

#main model
class Todo(BaseModel):
    title: str
    completed: bool
    id: int
    category: Category