import logging

from requests import get, Response

class Connection:
    def __init__(self, api_key: str, application_key: str) -> None:
        """
        Init connection.
        :param api_key: A generated API key from Ambient Weather.
        :param application_key: A generated application key from Ambient Weather.
        """
        self.api_key = api_key
        self.application_key = application_key

        self.logger = logging.Logger(__name__)

    def get_user_devices(self, ):
        try:
            response: Response = get(
                url="https://rt.ambientweather.net/v1/devices",
                params={
                    "applicationKey": self.application_key,
                    "apiKey": self.api_key
                }
            )
        except Exception as e:
            self.logger.error(e)
            return None
        result = response.json()
        print()
