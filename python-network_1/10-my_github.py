#!/usr/bin/python3
"""Uses the GitHub API with Basic Authentication to display the user's id."""
import requests
import sys


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
