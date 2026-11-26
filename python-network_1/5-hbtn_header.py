#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id response header."""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
