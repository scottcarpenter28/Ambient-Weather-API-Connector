import unittest

# from ambient_weather_api.datatypes.device import Device, Info
from ambient_weather_api.datatypes.weather_data import WeatherData


class TestDataTypes(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_user_devices_response = {
            "macAddress": "00:00:00:00:00:00",
            "info": {
            "name": "My Weather Station",
            "location": "Home"
            },
            "lastData": {
            "dateutc": 1515436500000,
            "date": "2018-01-08T18:35:00.000Z",
            "winddir": 58,
            "windspeedmph": 0.9,
            "windgustmph": 4,
            "maxdailygust": 5,
            "windgustdir": 61,
            "winddir_avg2m": 63,
            "windspdmph_avg2m": 0.9,
            "winddir_avg10m": 58,
            "windspdmph_avg10m": 0.9,
            "tempf": 66.9,
            "humidity": 30,
            "baromrelin": 30.05,
            "baromabsin": 28.71,
            "tempinf": 74.1,
            "humidityin": 30,
            "hourlyrainin": 0,
            "dailyrainin": 0,
            "monthlyrainin": 0,
            "yearlyrainin": 0,
            "feelsLike": 66.9,
            "dewPoint": 34.45380707462477
            }
        }

        self.mock_device_data_response = {
            "dateutc": 1515436500000,
            "date": "2018-01-08T18:35:00.000Z",
            "winddir": 58,
            "windspeedmph": 0.9,
            "windgustmph": 4,
            "maxdailygust": 5,
            "windgustdir": 61,
            "winddir_avg2m": 63,
            "windspdmph_avg2m": 0.9,
            "winddir_avg10m": 58,
            "windspdmph_avg10m": 0.9,
            "tempf": 66.9,
            "humidity": 30,
            "baromrelin": 30.05,
            "baromabsin": 28.71,
            "tempinf": 74.1,
            "humidityin": 30,
            "hourlyrainin": 0,
            "dailyrainin": 0,
            "monthlyrainin": 0,
            "yearlyrainin": 0,
            "feelsLike": 66.9,
            "dewPoint": 34.45380707462477
        }

    def test_weather_data(self):
        result = WeatherData(**self.mock_device_data_response)
        self.assertTrue(isinstance(result, WeatherData))

if __name__ == "__main__":
    unittest.main()