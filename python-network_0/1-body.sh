#!/bin/bash
# Sends a GET request to a URL and displays the body only if the status code is 200
response=$(curl -s -w "\n%{http_code}" "$1"); code=$(echo "$response" | tail -n1); [ "$code" -eq 200 ] && echo "$response" | sed '$d'
