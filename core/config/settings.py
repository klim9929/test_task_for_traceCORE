import os
from dotenv import load_dotenv

load_dotenv()

"""Здесь хранятся константы в т.ч. ендпойнты"""

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL должен быть определен в .env")


CREATE_USER_LIST = f"{BASE_URL}/user/createWithList"
GET_USER = f"{BASE_URL}/user/{{username}}"