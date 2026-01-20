from core.api.user_api import UserApi
from core.utils.api.user_model import User

"""
Тест создания пользователя и проверки его существования,
Может быть доработан параметризацией, маркерами и т.д.
"""

def test_create_user(user_data):
    create_response = UserApi.create_user_with_list([user_data.as_dict()])
    assert create_response.status_code == 200, f"Создание пользователя не удалось: {create_response.text}"

    get_response = UserApi.get_user_by_username(user_data.username)
    assert get_response.status_code == 200, f"Получение пользователя не удалось: {get_response.text}"

    user = User(**get_response.json())
    assert user.username == user_data.username
    assert user.firstName == user_data.firstName
    assert user.email == user_data.email
