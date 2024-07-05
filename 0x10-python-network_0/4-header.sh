#!/bin/bash
# Perform a GET with a Custom Header
curl -s -X GET "$1" -H "X-School-User-Id: 98"
