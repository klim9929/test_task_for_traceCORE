import pydantic

class User(pydantic.BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str
    userStatus: int