from pydantic import BaseModel, Field, ValidationError

class Person(BaseModel):
    fist_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: int | None = Field(None, ge=0, le=120)