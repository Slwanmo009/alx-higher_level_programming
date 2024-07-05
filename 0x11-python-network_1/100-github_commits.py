#!/usr/bin/python3
"""
This script retrieves the 10 most recent commits from a GitHub repository
by a specific user using the GitHub API.
It takes two arguments:
- Repository name
- Owner (username) of the repository
"""

import requests
import sys

def list_commits(repo_name, owner_name):
    """
    Retrieves and prints the 10 most recent commits from a GitHub repository.

    Args:
        repo_name (str): Name of the GitHub repository.
        owner_name (str): Owner (username) of the GitHub repository.
    """
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    params = {
        'per_page': 10,
        'sha': 'master'  # Assuming we want commits from the master branch
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing GitHub API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./list_commits.py <repo_name> <owner_name>")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    list_commits(repo_name, owner_name)
