from core.api.http_client import HttpClient
from core.config.settings import CREATE_USER_LIST, GET_USER


class UserApi:
    """API-клиент для работы с пользователями."""

    @staticmethod
    def create_user_with_list(users):
        return HttpClient.post(CREATE_USER_LIST, json=users)

    @staticmethod
    def get_user_by_username(username):
        return HttpClient.get(GET_USER.format(username=username))