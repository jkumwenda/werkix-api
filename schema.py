from pydantic import BaseModel, Field, EmailStr


class NewsSchema(BaseModel):
    role: str
    description: str
