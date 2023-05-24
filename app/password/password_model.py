from pydantic import BaseModel


class UserInDB(BaseModel):
    hashed_password: str
