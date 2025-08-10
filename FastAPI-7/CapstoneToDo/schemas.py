from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Priority(int, Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4
    CRITICAL = 5

class TaskBase(BaseModel):
    title:str = Field(min_length=1,max_length=50, description="Task baslığı")
    description:str = Field(default=None, max_length=200)
    status:TaskStatus = Field(default_factory=TaskStatus.PENDING, description="Task durumu")
    priority:Priority = Field(default_factory=Priority.MEDIUM, description="öncelik durumu")


class TaskCreate(TaskBase):
    pass # ID olmadan task oluşturma

class Task(TaskBase): # aslında bu TaskResponse, yani kullanıcıya gösterdiğim Task bilgileri
    """API response için schema"""
    id:int
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime | None = Field(default=None)


class TaskUpdate(BaseModel):
    title: str | None = Field(min_length=1,max_length=50, validate_default=True, description="Task baslığı")
    description: str | None = Field(default=None, max_length=200)
    status: TaskStatus | None = Field(default=None, description="Task durumu")
    priority: Priority | None = Field(default=None, description="öncelik durumu")





