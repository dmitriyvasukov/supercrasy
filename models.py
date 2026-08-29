from pydantic import BaseModel


class UserModel(BaseModel):
    username : str
    loh_count : float
    summary : str
    