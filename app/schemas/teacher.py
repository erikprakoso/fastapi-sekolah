from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class TeacherSchema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    subject: Optional[str]=None
    email: Optional[str]=None

    class Config:
        orm_mode = True

class RequestTeacher(BaseModel):
    parameter: TeacherSchema = Field(...)

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]