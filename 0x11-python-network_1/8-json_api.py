#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. It expects JSON formatted response and handles different scenarios:
- If JSON is properly formatted and not empty, it displays [<id>] <name>.
- If JSON is invalid, it displays "Not a valid JSON".
- If JSON is empty, it displays "No result".
"""

import requests
import sys

def search_user(q):
    """
    Sends a POST request to search for a user based on the given letter.
    
    Args:
        q (str): The letter to search for.

    Returns:
        str: The formatted response or error message.
    """
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        json_data = response.json()
        if json_data:
            return f"[{json_data['id']}] {json_data['name']}"
        else:
            return "No result"
    except requests.exceptions.RequestException as e:
        return f"Not a valid JSON"

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    result = search_user(q)
    print(result)
