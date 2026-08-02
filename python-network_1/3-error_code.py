#!/usr/bin/python3
"""Send a request and print the response body or the HTTP error code."""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
