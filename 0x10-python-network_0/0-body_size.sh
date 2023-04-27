#!/bin/bash
# A bash script that takes in a URL and sends a request to the URL
curl -s "$1" | wc -c
