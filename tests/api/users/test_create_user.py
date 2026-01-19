import requests
import pytest

from core.data.test_data.gen_users import UserData
from core.utils.api.user_model import User



def test_create_user():
    base_url = "https://petstore.swagger.io/v2/"
    create_user_endpoint = f"{base_url}user/createWithList"
    user_data = UserData().data
    user_list = [user_data]
    print(user_list)
    response = requests.post(
        url=create_user_endpoint,
        json=user_list
    )
    print(response.json())
    username = user_list[0].get("username")
    print("username", username)
    get_user_endpoint = f"{base_url}user/{username}"
    get_status = requests.get(get_user_endpoint)
    assert get_status.status_code == 200