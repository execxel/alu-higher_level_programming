#!/bin/bash
# Sends a request to the URL in the first argument and displays the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}" "$1"
