# GitHubApi567
# hw4a
# Github User Repositories
This program is designed to retrieve a list of the repositories owned by a given GitHub user along with the number of commits made in each repository. The program utilizes the GitHub API to retrieve this information.

# Files in this repository
hw4a.py - This file contains a function called get_user_repos that takes a GitHub user ID as input and returns a list of tuples containing the repository name and its commit count for the given user_id. The possible return values are:

A list of tuples, each tuple containing the name of the repository and its commit count
An empty list, if an error occurs
Testhw4a.py - This file contains unit tests for the get_user_repos function. It includes test cases for successful retrievals and error cases.

# How to run the tests
To run the tests, make sure you have Python installed on your machine, then navigate to the directory containing the Testhw4a.py file and run the following command:
python3 -m unittest Testhw4a -v

This will run all of the tests and output the results to the console.

# Notes on the get_user_repos function
The get_user_repos function includes error handling to ensure that the program will not crash if an invalid user ID is provided or if the GitHub API is unavailable. If an error occurs, the function returns an empty list.

[![Ameya172](https://circleci.com/gh/Ameya172/SSW567.svg?style=svg)](https://app.circleci.com/pipelines/github/Ameya172/SSW567?branch=main&filter=all)
=======

>>>>>>> origin/main

