from pydantic import BaseModel, field_validator

class Model(BaseModel):
    values: list[int]
    
    @field_validator("values")
    def split_string_values(csl, v):
        if isinstance(v, str):
            return v.split(",")
        return v