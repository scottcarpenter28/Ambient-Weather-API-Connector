from os import getenv
import unittest

from dotenv import load_dotenv
from ambient_weather_api.connection import Connection


class TestAPIIntegration(unittest.TestCase):
    def setUp(self):
        self.conn = Connection(
            api_key=getenv("API_KEY"),
            application_key=getenv("APPLICATION_KEY")
        )

    def tearDown(self):
        pass

    def test_get_user_devices(self):
        result = self.conn.get_user_devices()
        self.assertEqual(len(result), 1)

    def test_get_weather_data(self):
        stations = self.conn.get_user_devices()
        result = self.conn.get_device_data(station=stations[0])
        self.assertEqual(len(result), 288)

if __name__ == "__main__":
    unittest.main()