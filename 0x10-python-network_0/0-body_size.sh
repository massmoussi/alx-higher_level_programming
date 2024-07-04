#!/bin/bash
# Bash Script to display the response size in bytes

curl -sI "$1" | grep 'Content-Length' | sed 's/^Content-Length: //'
