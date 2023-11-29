from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Question(Base):
    __tablename__ = "question"
    id=Column(Integer, primary_key=True)
    subject=Column(String(20), nullable=False) #글자 수 제한
    content=Column(Text, nullable=False) #글자 수 제한 안 됨
    create_date=Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="question_users")
    modify_date = Column(DateTime, nullable=True)

class Answer(Base):
    __tablename__ = "answer"
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="answer_users")
    modify_date = Column(DateTime, nullable=True)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(10), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(20), unique=True, nullable=False)

# class Place(Base):
#     __tablename__ = "place"
#     id = Column()