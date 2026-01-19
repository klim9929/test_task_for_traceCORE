import requests


class HttpClient:
    """HTTP-клиент для выполнения запросов."""

    @staticmethod
    def post(url, **kwargs):
        return requests.post(url, **kwargs)

    @staticmethod
    def get(url, **kwargs):
        return requests.get(url, **kwargs)
