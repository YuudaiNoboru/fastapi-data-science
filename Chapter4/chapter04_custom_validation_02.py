from pydantic import BaseModel, EmailStr, ValidationError, model_validator

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str
    @model_validator(mode="after")
    def password_match(cls, values):
        password = values.get("password")
        password_confirmation = values.get("password_confirmation")
        if password != password_confirmation:
            raise ValueError("Passwords don't match")
        return values
