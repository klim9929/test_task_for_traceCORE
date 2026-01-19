import requests
import pytest

from core.config.settings import CREATE_USER_LIST, GET_USER
from core.data.test_data.gen_users import UserData
from core.utils.api.user_model import User



def test_create_user():
    user_data = UserData().data
    user_list = [user_data]
    print(user_list)
    response = requests.post(
        url=CREATE_USER_LIST,
        json=user_list
    )
    print(response.json())
    username = user_list[0].get("username")
    #print("username", username)
    get_status = requests.get(GET_USER.format(username=username))
    assert get_status.status_code == 200