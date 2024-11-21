import unittest
from unittest.mock import patch
from api_client import ApiClient
from repository import UserRepository

class TestUserRepository(unittest.TestCase):
    @patch('api_client.ApiClient.get')
    def test_get_users(self, mock_get):
        mock_get.return_value.json.return_value = [
            {'id': 1, 'name': 'Leanne Graham'},
            {'id': 2, 'name': 'Ervin Howell'}
        ]

        api_client = ApiClient()
        user_repository = UserRepository(api_client)
        users = user_repository.get_users()

        self.assertEqual(users, [
            {'id': 1, 'name': 'Leanne Graham'},
            {'id': 2, 'name': 'Ervin Howell'}
        ])