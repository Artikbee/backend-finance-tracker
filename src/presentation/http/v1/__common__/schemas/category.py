from pydantic import BaseModel


class CreateCategorySchema(BaseModel):
    name: str
