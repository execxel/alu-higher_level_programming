#!/bin/bash
# Sends a request to the URL in the first argument and displays the response body size in bytes
curl -s -o /dev/null -w "%{size_download}" "$1"