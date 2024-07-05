#!/usr/bin/python3
"""
This script retrieves the GitHub user ID using Basic Authentication with a personal access token (PAT).
It takes two arguments:
- Username: Your GitHub username.
- Password: Your personal access token (PAT) as the password (only read:user permission needed).
"""

import requests
import sys

def get_github_user_id(username, password):
    """
    Retrieves the GitHub user ID using Basic Authentication with a personal access token (PAT).

    Args:
        username (str): Your GitHub username.
        password (str): Your personal access token (PAT) as the password.

    Returns:
        str: The GitHub user ID.
    """
    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'token {password}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        user_data = response.json()
        return str(user_data['id'])
    except requests.exceptions.RequestException as e:
        print(f"Error accessing GitHub API: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./github_user_id.py <username> <password>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    user_id = get_github_user_id(username, password)
    
    if user_id:
        print(f"GitHub User ID: {user_id}")
