import logging
from typing import Any, Dict

from ambient_weather_api.datatypes.device import Device
from ambient_weather_api.datatypes.weather_data import WeatherData

from requests import get, Response
from requests import codes
from requests.exceptions import JSONDecodeError

class Connection:
    def __init__(self, api_key: str, application_key: str, timeout: float | None = 10) -> None:
        """
        Init connection.
        :param api_key: A generated API key from Ambient Weather.
        :param application_key: A generated application key from Ambient Weather.
        """
        self.api_key = api_key
        self.application_key = application_key
        self.timeout = timeout

        self.logger = logging.Logger(__name__)

    def _get(self, url: str, params: Dict[str, Any] = {}) -> dict | None:
        """
        Makes a get request to the API. 
        :param url: The url of the request.
        :param params: An optional dictionary of parameters. The applicaiton and api keys are added before the request.
        :return : None if an error occurred, or dictionary of the response if ok.
        """
        params.update({"applicationKey": self.application_key, "apiKey": self.api_key})

        try:
            response: Response = get(url=url, params=params, timeout=self.timeout)
        except TimeoutError as e:
            self.logger.error(e)
            return None
        
        if not response.status_code == codes.ok:
            self.logger.error(f"{response.status_code}: {response.text}")
            return None
        
        try:
            return response.json()
        except JSONDecodeError as e:
            self.logger.error(e)
            return None
        

    def get_user_devices(self, ):
        result = self._get("https://rt.ambientweather.net/v1/devices")
        print()
