import pytest

from core.data.test_data.gen_users import UserData


@pytest.fixture()
def user_data():
    """Возвращающает экземпляр сгенерированных данных пользователя."""
    return UserData()