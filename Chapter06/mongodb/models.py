from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, Field

class PyObjectID(ObjectId):
    @classmethod
    def __get_validator__(cls):
        yield cls.validete
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

class MongoBaseModel(BaseModel):
    id: PyObjectID = Field(default_factory=PyObjectID, alias="_id")
    class Config:
        json_encoders = {ObjectId: str}

class CommentBase(BaseModel):
    publication_date: datetime = Field(default_factory=datetime.now)
    coment: str

class Comment(CommentBase):
    pass

class CommentCreate(CommentBase):
    pass

class PostBase(MongoBaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)

class PostParticialUpdate(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    comments: list[Comment] = Field(default_factory=list)