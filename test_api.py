import unittest
from api_project import channel_id, get_5_videos, user_input
from unittest.mock import patch


class TestAPI(unittest.TestCase):

    def test_user_input(self):

        with patch('builtins.input', side_effect=['pewdiepie',  ' ', None]):
            self.assertEqual(user_input(), 'pewdiepie')
            self.assertEqual(user_input(), ' ')
            self.assertIsNone(user_input())


if __name__ == '__main__':
    unittest.main()
