#!/usr/bin/python3

"""
    Post request things
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    r = requests.post(url, data=email)
    print("Your email is : {}".format(sys.argv[2]))
