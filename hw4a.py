import requests
import json

def get_user_repos(user_id):
    # Make a request to get the list of user repositories
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code != 200:
        print(f"Failed to get user repositories for {user_id}. Error: {response.content}")
        return []

    # Parse the JSON response to get the repository names and commit counts
    repo_commits = []
    repos = json.loads(response.content)
    for repo in repos:
        repo_name = repo["name"]
        commit_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commit_response = requests.get(commit_url)
        commit_count = len(json.loads(commit_response.content))
        repo_commits.append((repo_name, commit_count))

    return repo_commits
