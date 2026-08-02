#!/usr/bin/python3
"""Send a POST request with an email and display the response body."""
import requests
import sys


if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=payload)
    print(response.text)
