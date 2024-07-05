#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email parameter and displays the decoded response body.

Usage:
    ./post_request.py <URL> <email>

Example:
    ./post_request.py http://0.0.0.0:5000/test test@example.com
"""

import urllib.parse
import urllib.request
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to be sent as a parameter.

    Prints:
        The decoded response body of the POST request.
    """
    # Encode the data to be sent
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        # Send the POST request and handle the response
        with urllib.request.urlopen(url, data=data) as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.URLError as e:
        print(f"Error accessing URL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./post_request.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
