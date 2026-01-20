import requests
import logging
import json

logger = logging.getLogger(__name__)

"""Здесь можно дописать методы для полноценной работы с http клиентом"""

class HttpClient:
    @staticmethod
    def post(url, **kwargs):
        logger.info(f"POST {url}")
        if 'json' in kwargs:
            logger.info(f"Request JSON: {json.dumps(kwargs['json'], ensure_ascii=False, indent=2)}")

        response = requests.post(url, **kwargs)

        logger.info(f"STATUS CODE: {response.status_code} {response.reason} ({response.elapsed.total_seconds():.2f}s)")
        try:
            json_data = response.json()
            logger.info(f"Response JSON: {json.dumps(json_data, ensure_ascii=False, indent=2)}")
        except Exception:
            logger.info(f"Response text: {response.text}")

        return response

    @staticmethod
    def get(url, **kwargs):
        logger.info(f"GET {url}")
        response = requests.get(url, **kwargs)

        logger.info(f"STATUS CODE: {response.status_code} {response.reason} ({response.elapsed.total_seconds():.2f}s)")
        try:
            json_data = response.json()
            logger.info(f"Response JSON: {json.dumps(json_data, ensure_ascii=False, indent=2)}")
        except Exception:
            logger.info(f"Response text: {response.text}")

        return response