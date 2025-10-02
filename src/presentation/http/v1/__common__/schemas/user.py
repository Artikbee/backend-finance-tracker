from pydantic import BaseModel


class RegisterUserSchema(BaseModel):
    email: str
    password: str


class LoginUserSchema(BaseModel):
    email: str
    password: str


class UpdateUserSchema(BaseModel):
    last_name: str
    first_name: str
    is_active: bool


class LogoutUserSchema(BaseModel):
    refresh_token: str
