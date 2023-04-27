#!/bin/bash
# Sends a request to curl displaying the status of code

curl -s -o /dev/null -w "%{http_code}" "$1"
