import logging
from typing import Any, Dict, List
import pprint

from ambient_weather_api.datatypes.device import Device
from ambient_weather_api.datatypes.weather_data import WeatherData

from requests import get, Response
from requests import Timeout, HTTPError
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
            response.raise_for_status()
            return response.json()
        except Timeout as e:
            self.logger.error(e)
            return None
        except HTTPError as e:
            self.logger.error(e)
            return None
        except JSONDecodeError as e:
            self.logger.error(e)
            return None

    def get_user_devices(self, ) -> List[Device]:
        result = self._get("https://rt.ambientweather.net/v1/devices")
        if result is None:
            return []
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(result)
        return [Device(**station) for station in result]
