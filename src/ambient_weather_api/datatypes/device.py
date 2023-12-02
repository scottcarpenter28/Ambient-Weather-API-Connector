from pydantic import BaseModel
from ambient_weather_api.datatypes.weather_data import WeatherData


class Info(BaseModel):
    name: str
    location: str


class Device(BaseModel):
    macAddress: str
    info: Info
    lastData: WeatherData