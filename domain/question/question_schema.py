import datetime
from pydantic import BaseModel, field_validator
from domain.answer.answer_schema import Answer
from domain.user.user_schema import User

class Question(BaseModel):
    id:int
    subject:str | None = "didn't write subject"
    content:str
    create_date:datetime.datetime
    answers: list[Answer] = []
    user:User | None

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('null is not allowed!!')
        return v

class QuestionList(BaseModel):
    total: int = 0
    question_list : list[Question] = []

class QuestionUpdate(QuestionCreate):
    question_id:int