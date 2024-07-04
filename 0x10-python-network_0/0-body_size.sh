#!/bin/bash
# Takes an URL, sends a requst to it, and dsplys the size of the body

url="$1"

curl -s -o /dev/null -w "%{size_download}\n" "$url"
