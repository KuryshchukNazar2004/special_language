import unittest
from api_client import ApiClient

class TestApiClient(unittest.TestCase):
    def test_get(self):
        api_client = ApiClient()
        response = api_client.get('/users')
        self.assertEqual(response.status_code, 200)