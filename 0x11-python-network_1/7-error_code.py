#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response. If the HTTP status code
is greater than or equal to 400, it prints an error code.
"""

import requests
import sys

def fetch_url(url):
    """
    Fetches the URL and displays the body of the response.
    If the status code is 400 or higher, prints an error code.

    Args:
        url (str): The URL to fetch.
    """
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
