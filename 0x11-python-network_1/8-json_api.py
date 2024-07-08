#!/usr/bin/python3

"""
Script Perform a POST check if response is empty
check if reponse is json
"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        print("No result")
    else:
        if sys.argv[1]:
            param = {'q': sys.argv[1]}
        else:
            param = {'q': ''}

        r = requests.post(url, data=param)
        if not r.content:
            print("No result")
        else:
            try:
                response = r.json()
                print("[{}] {}".format(response['id'], response['name']))
            except ValueError:
                print("Not a valid JSON")
