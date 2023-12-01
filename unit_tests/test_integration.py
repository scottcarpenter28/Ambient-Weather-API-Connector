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
        self.conn.get_user_devices()

if __name__ == "__main__":
    unittest.main()