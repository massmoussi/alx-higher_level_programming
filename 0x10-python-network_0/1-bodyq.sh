#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# Only display the body of a 200 status code response

url="$1"

response=$(curl -s -w "%{http_code}" "$url")
body=$(echo "$response" | sed -e 's/[0-9]\{3\}$//')
status_code=$(echo "$response" | tail -c 4)

if [ "$status_code" -eq 200 ]; then
  echo "$body"
fi
