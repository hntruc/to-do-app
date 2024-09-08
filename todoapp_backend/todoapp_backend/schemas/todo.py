from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'Todo'

    id = Column(Integer, primary_key=True)
    task = Column(String(100))
    done = Column(Boolean)

    class Config:
        orm_mode = True
        from_attributes = True

class GetTodo(BaseModel):
    id: int
    task: str
    done: bool

    
    class Config:
        orm_mode = True
        from_attributes = True

class PostTodo(BaseModel):
    id: int
    task: str = Field(..., max_length=100)
    done: bool

    
    class Config:
        orm_mode = True
        from_attributes = True

class PutTodo(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    done: Optional[bool]

    
    class Config:
        orm_mode = True
        from_attributes = True
