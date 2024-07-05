#!/bin/bash
# Make reqst that cause specif response
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
