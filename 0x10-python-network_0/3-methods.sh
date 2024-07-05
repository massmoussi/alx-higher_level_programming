#!/bin/bash
# scrpt disply Allowed http methds
curl -s -I "$1" | awk '/^Allow:/ {sub(/^Allow: /, ""); print}'
