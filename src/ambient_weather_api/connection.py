from datetime import datetime
import time
import logging
from typing import Any, Callable, Dict, List

from ambient_weather_api.datatypes.device import Device
from ambient_weather_api.datatypes.weather_data import WeatherData

from requests import get, Response
from requests import Timeout, HTTPError
from requests.exceptions import JSONDecodeError


# Time that the API was last called. Limit to 1 request per second.
last_call_time: int | None = None

# Custom data type
OptionalListDict = List[Dict[str, Any]] | None

def LimitRate(func: Callable) -> Callable:
    def check_last_call(*args, **kwargs):
        global last_call_time
        current_time: int = int(time.time())
        if last_call_time is not None:
            while current_time <= last_call_time + 1:
                time.sleep(1)
                current_time = int(time.time())
        last_call_time = current_time

        return func(*args, **kwargs)
    return check_last_call


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

    @LimitRate
    def _get(self, url: str, params: Dict[str, Any] = {}) -> OptionalListDict:
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

    def get_user_devices(self) -> List[Device]:
        """
        Gets a list of user devices.
        :return: A list of all devices.
        """
        result: OptionalListDict = self._get("https://rt.ambientweather.net/v1/devices")
        return [] if result is None else [Device(**station) for station in result]
    
    def get_device_data(self, station: Device, end_date: datetime | None = None, limit: int = 288) -> List[WeatherData]:
        """
        Gets a list of data from the device.
        :param station: The weather station to get data for.
        :param end_date: Optional date to end on. Sadly no control to select start date.
        :param limit: The maximum data points to return. Max limit is 288.
        :return: A list of all matching weather data.
        """
        params: OptionalListDict = {}
        if end_date is not None:
            params["endDate"] = int(end_date.timestamp * 1000)

        if limit <= 0 or limit > 288:
            limit = 288
        params["limit"] = limit
        
        result = self._get(f"https://rt.ambientweather.net/v1/devices/{station.macAddress}", params)
        return [] if result is None else [WeatherData(**data) for data in result]
