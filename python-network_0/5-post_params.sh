#!/bin/bash
# Sends a POST request with email and subject parameters to a URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
