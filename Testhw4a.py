import unittest
from hw4a import get_user_repos

class TestGetUserRepos(unittest.TestCase):
    def test_get_user_repos_success(self):
        user_id = "Ameya172"
        expected_result = [('GitHubApi567', 9), ("SSW567", 20)]
        self.assertEqual(get_user_repos(user_id), expected_result)

    def test_get_user_repos_error(self):
        user_id = "nonexistent_user"
        expected_result = []
        self.assertEqual(get_user_repos(user_id), expected_result)

if __name__ == '__main__':
    unittest.main()
