from datetime import date
from enum import Enum
from pydantic import BaseModel, ValidationError

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class Address(BaseModel):
    postal_code: str
    city: str
    country: str
    street_address: str

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: list[str]
    address: Address

person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    birthdate=date(1991, 1, 1),
    interests=["travel", "sports"],
    address=Address(
        postal_code="12345",
        city="Anytown",
        country="USA",
        street_address="123 Main Street",
    ),
)

person_dict = person.model_dump(include={"first_name", "last_name", "address", "postal_code", "street_address"})
print(person_dict)