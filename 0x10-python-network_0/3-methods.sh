#!/bin/bash
# A bash script that takes in URL and displays all HTTP methods the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
