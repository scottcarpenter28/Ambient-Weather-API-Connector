from datetime import datetime
from pydantic import BaseModel


class WeatherData(BaseModel):
    baromabsin: float
    baromrelin: float
    battin: int
    battout: int
    dailyrainin: float
    date: datetime
    dateutc: float
    dewPoint: float
    dewPointin: float
    eventrainin: float
    feelsLike: float
    feelsLikein: float
    hourlyrainin: float
    humidity: float
    humidityin: float
    lastRain: datetime
    maxdailygust: float
    monthlyrainin: float
    solarradiation: float
    tempf: float
    tempinf: float
    tz: str | None = None
    uv: float
    weeklyrainin: float
    winddir: int
    winddir_avg10m: int
    windgustmph: float
    windspdmph_avg10m: float
    windspeedmph: float
    yearlyrainin: float

    # Todo: Unit conversions
