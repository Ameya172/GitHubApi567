import unittest
from unittest.mock import patch, MagicMock
from hw4a import get_user_repos

class TestGetUserRepos(unittest.TestCase):

    @patch('hw4a.requests.get')
    def test_get_user_repos_success(self, mock_get):
        # Mock the response from the API
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"name": "GitHubApi567", "stargazers_count": 9},
            {"name": "SSW567", "stargazers_count": 20}
        ]
        mock_get.return_value = mock_response

        user_id = "Ameya172"
        expected_result = [('GitHubApi567', 9), ("SSW567", 20)]
        self.assertEqual(get_user_repos(user_id), expected_result)

    @patch('hw4a.requests.get')
    def test_get_user_repos_error(self, mock_get):
        # Mock the response from the API
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        user_id = "nonexistent_user"
        expected_result = []
        self.assertEqual(get_user_repos(user_id), expected_result)

if __name__ == '__main__':
    unittest.main()
