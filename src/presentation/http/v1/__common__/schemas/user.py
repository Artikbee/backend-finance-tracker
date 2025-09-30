from pydantic import BaseModel


class RegisterUserSchema(BaseModel):
    email: str
    password: str
