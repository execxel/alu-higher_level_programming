#!/usr/bin/python3
"""Send a POST request with an email and display the response body."""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
