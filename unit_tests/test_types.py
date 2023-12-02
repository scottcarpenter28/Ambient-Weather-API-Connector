import unittest

from ambient_weather_api.datatypes.device import Device
from ambient_weather_api.datatypes.weather_data import WeatherData


class TestDataTypes(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_user_devices_response = {   
            'info': {   
                'coords': {   
                    'address': '1 ABC St, Somewhere, NY 00000, USA',
                    'coords': {   
                        'lat': 00.000,
                        'lon': 00.000
                        },
                    'elevation': 0.0,
                    'geo': {
                        'coordinates': [00.000, 00.000],
                        'type': 'Point'
                    },
                    'location': 'Somewhere'
                },
                'name': 'Weatherstation'
            },
            'lastData': {   
                'baromabsin': 29.584,
                'baromrelin': 29.584,
                'battin': 1,
                'battout': 1,
                'dailyrainin': 0.039,
                'date': '2023-12-02T14:55:00.000Z',
                'dateutc': 1701528900000,
                'dewPoint': 45.78,
                'dewPointin': 48.4,
                'eventrainin': 0.331,
                'feelsLike': 47.7,
                'feelsLikein': 66,
                'hourlyrainin': 0,
                'humidity': 93,
                'humidityin': 53,
                'lastRain': '2023-12-02T14:06:00.000Z',
                'maxdailygust': 2.2,
                'monthlyrainin': 0.331,
                'solarradiation': 48.07,
                'tempf': 47.7,
                'tempinf': 66,
                'tz': 'America/New_York',
                'uv': 0,
                'weeklyrainin': 0.539,
                'winddir': 113,
                'winddir_avg10m': 106,
                'windgustmph': 0,
                'windspdmph_avg10m': 0,
                'windspeedmph': 0,
                'yearlyrainin': 27.965
            },
            'macAddress': '00:00:00:00:00:00'
        }

        self.mock_device_data_response = {   
                'baromabsin': 29.584,
                'baromrelin': 29.584,
                'battin': 1,
                'battout': 1,
                'dailyrainin': 0.039,
                'date': '2023-12-02T14:55:00.000Z',
                'dateutc': 1701528900000,
                'dewPoint': 45.78,
                'dewPointin': 48.4,
                'eventrainin': 0.331,
                'feelsLike': 47.7,
                'feelsLikein': 66,
                'hourlyrainin': 0,
                'humidity': 93,
                'humidityin': 53,
                'lastRain': '2023-12-02T14:06:00.000Z',
                'maxdailygust': 2.2,
                'monthlyrainin': 0.331,
                'solarradiation': 48.07,
                'tempf': 47.7,
                'tempinf': 66,
                'tz': 'America/New_York',
                'uv': 0,
                'weeklyrainin': 0.539,
                'winddir': 113,
                'winddir_avg10m': 106,
                'windgustmph': 0,
                'windspdmph_avg10m': 0,
                'windspeedmph': 0,
                'yearlyrainin': 27.965
            }

    def test_weather_data(self):
        result = WeatherData(**self.mock_device_data_response)
        self.assertTrue(isinstance(result, WeatherData))

    def test_device_data(self):
        result = Device(**self.mock_user_devices_response)
        self.assertTrue(isinstance(result, Device))

if __name__ == "__main__":
    unittest.main()