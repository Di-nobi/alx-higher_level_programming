#!/bin/bash
# Sends a JSON POST request to URL
curl -s -H "Content-Tye: application/json" -d "$(cat "$2")" "$1"
