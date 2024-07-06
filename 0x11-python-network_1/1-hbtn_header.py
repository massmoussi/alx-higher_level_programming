#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        headers = response.headers
        print(headers['X-Request-Id'])
