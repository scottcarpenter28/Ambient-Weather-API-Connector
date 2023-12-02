from typing import List
from pydantic import BaseModel
from ambient_weather_api.datatypes.weather_data import WeatherData


class Coord(BaseModel):
    lat: float
    lon: float


class Geo(BaseModel):
    coordinates: List[float]
    type: str


class CoordInfo(BaseModel):
    address: str
    coords: Coord
    elevation: float
    geo: Geo
    location: str


class Info(BaseModel):
    coords: CoordInfo
    name: str


class Device(BaseModel):
    info: Info
    lastData: WeatherData
    macAddress: str
    