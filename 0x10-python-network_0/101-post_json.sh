#!/bin/bash
# Perform a POST requst with a prmtrs in JSON
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
