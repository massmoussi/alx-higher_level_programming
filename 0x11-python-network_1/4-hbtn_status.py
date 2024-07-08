#!/usr/bin/python3

"""
This script fetches https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
