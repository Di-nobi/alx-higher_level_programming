#!/bin/bash
# A bash script that takes in a URL and sends a request to the URL
# and displays the size body of the response
curl -s "$1" | wc -c
