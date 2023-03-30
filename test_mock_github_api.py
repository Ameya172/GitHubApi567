import unittest
from unittest.mock import patch, MagicMock
from my_github_api import get_user_repos

class TestGetUserRepos(unittest.TestCase):
    
    @patch('my_github_api.requests.get')
    def test_get_user_repos_success(self, mock_get):
        # Define the mocked response
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {'name': 'GitHubApi567', 'stargazers_count': 9},
            {'name': 'SSW567', 'stargazers_count': 20}
        ]
        mock_response.status_code = 200
        
        # Configure the mock object to return the mocked response
        mock_get.return_value = mock_response
        
        # Define the expected result
        expected_result = [('GitHubApi567', 9), ("SSW567", 20)]
        
        # Call the function and check the result
        result = get_user_repos("Ameya172")
        self.assertEqual(result, expected_result)
        
        # Check that the mock object was called with the correct arguments
        mock_get.assert_called_once_with('https://api.github.com/users/Ameya172/repos')

    @patch('my_github_api.requests.get')
    def test_get_user_repos_error(self, mock_get):
        # Define the mocked response
        mock_response = MagicMock()
        mock_response.status_code = 404
        
        # Configure the mock object to return the mocked response
        mock_get.return_value = mock_response
        
        # Define the expected result
        expected_result = []
        
        # Call the function and check the result
        result = get_user_repos("nonexistent_user")
        self.assertEqual(result, expected_result)
        
        # Check that the mock object was called with the correct arguments
        mock_get.assert_called_once_with('https://api.github.com/users/nonexistent_user/repos')

if __name__ == '__main__':
    unittest.main()

