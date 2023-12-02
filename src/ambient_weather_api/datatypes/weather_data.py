from datetime import datetime
from pydantic import BaseModel


class WeatherData(BaseModel):
    dateutc: float
    date: datetime
    winddir: int
    windspeedmph: float
    windgustmph: float
    maxdailygust: float
    windgustdir: int
    winddir_avg2m: int
    windspdmph_avg2m: float
    winddir_avg10m: int
    windspdmph_avg10m: float
    tempf: float
    humidity: int
    baromrelin: float
    baromabsin: float
    tempinf: float
    humidityin: int
    hourlyrainin: float
    dailyrainin: float
    monthlyrainin: float
    yearlyrainin: float
    feelsLike: float
    dewPoint: float

    # Todo: Unit conversions
