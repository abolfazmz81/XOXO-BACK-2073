from pydantic import BaseModel


class input(BaseModel):
    name: str
    status: str
