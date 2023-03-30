# GitHubApi567
# hw5a
# Github User Repositories
This program is designed to retrieve a list of the repositories owned by a given GitHub user along with the number of commits made in each repository. The program utilizes the GitHub API to retrieve this information.

# Files in this repository
hw4a.py - This file contains a function called get_user_repos that takes a GitHub user ID as input and returns a list of tuples containing the repository name and its commit count for the given user_id. The possible return values are:

A list of tuples, each tuple containing the name of the repository and its commit count
An empty list, if an error occurs
Testhw4a.py - This file contains unit tests for the get_user_repos function. It includes test cases for successful retrievals and error cases.

# test_mock_github_api.py:
The file test_mock_github_api.py contains unit tests for the get_user_repos function in the hw4a.py file. The TestGetUserRepos class inherits from the unittest.TestCase class and includes two test methods:

test_get_user_repos_success: This test method mocks the response from the GitHub API using the unittest.mock.patch decorator and MagicMock object. It then calls the get_user_repos function with a valid user ID and checks if the function returns the expected result, which is a list of tuples containing the repository name and its commit count for the given user ID.

test_get_user_repos_error: This test method mocks the response from the GitHub API using the unittest.mock.patch decorator and MagicMock object. It then calls the get_user_repos function with an invalid user ID and checks if the function returns an empty list, which is the expected result when an error occurs.

The __name__ check at the end of the file ensures that the tests are only run when the file is executed directly and not when it is imported as a module.

# How to run the tests
To run the tests, make sure you have Python installed on your machine, then navigate to the directory containing the Testhw4a.py file and run the following command:
python3 -m unittest Testhw4a -v

This will run all of the tests and output the results to the console.

# Notes on the get_user_repos function
The get_user_repos function includes error handling to ensure that the program will not crash if an invalid user ID is provided or if the GitHub API is unavailable. If an error occurs, the function returns an empty list.

`[![Ameya172](https://circleci.com/gh/Ameya172/GitHubApi567.svg?style=svg)](https://app.circleci.com/pipelines/github/Ameya172/GitHubApi567?branch=HW05a_Mocking&filter=all)` 
