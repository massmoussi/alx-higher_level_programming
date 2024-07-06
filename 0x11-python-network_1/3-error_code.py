#!/usr/bin/python3
"""
    Handl diff Status Code with Try/expect
        if 200 it return utf-8 decoded response
        if Error appear expect handl it & retrn the code
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            html = r.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
