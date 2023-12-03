import unittest
from unittest.mock import Mock

from ambient_weather_api.connection import Connection
from ambient_weather_api.datatypes.weather_data import WeatherData
from ambient_weather_api.datatypes.device import Device


class TestConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = Connection(api_key="EXAMPLE_API_KEY", application_key="EXAMPLE_APPLICATION_KEY")
        self.mock_device_data_response = {
                    'baromabsin': 29.593,
                    'baromrelin': 29.593,
                    'battin': 1,
                    'battout': 1,
                    'dailyrainin': 0.039,
                    'date': '2023-12-02T16:00:00.000Z',
                    'dateutc': 1701532800000,
                    'dewPoint': 46.84,
                    'dewPointin': 48,
                    'eventrainin': 0.331,
                    'feelsLike': 48.2,
                    'feelsLikein': 66.2,
                    'hourlyrainin': 0,
                    'humidity': 95,
                    'humidityin': 52,
                    'lastRain': '2023-12-02T14:06:00.000Z',
                    'maxdailygust': 3.4,
                    'monthlyrainin': 0.331,
                    'solarradiation': 48.56,
                    'tempf': 48.2,
                    'tempinf': 66.2,
                    'uv': 0,
                    'weeklyrainin': 0.539,
                    'winddir': 47,
                    'winddir_avg10m': 95,
                    'windgustmph': 1.1,
                    'windspdmph_avg10m': 0.2,
                    'windspeedmph': 1.1,
                    'yearlyrainin': 27.965
                }
        
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
            'lastData': self.mock_device_data_response,
            'macAddress': '00:00:00:00:00:00'
        }

    def test_get_device_data(self):
        self.conn._get = Mock(return_value=[self.mock_device_data_response])
        result = self.conn.get_device_data(Device(**self.mock_user_devices_response))
        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], WeatherData))

    def test_get_device_data_error(self):
        self.conn._get = Mock(return_value=None)
        result = self.conn.get_device_data(Device(**self.mock_user_devices_response))
        self.assertEqual(len(result), 0)

    def test_get_user_devices(self):
        self.conn._get = Mock(return_value=[self.mock_user_devices_response])
        result = self.conn.get_user_devices()
        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], Device))

    def test_get_user_device_error(self):
        self.conn._get = Mock(return_value=None)
        result = self.conn.get_user_devices()
        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()