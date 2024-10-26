from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

class User(BaseModel):
    email: EmailStr
    website: HttpUrl

# Invalid email:

try:
    user = User(email="jdoes@exemple.com", website=HttpUrl("https://www.example.com"))
    print(user)

except ValidationError as e:
    print(str(e))