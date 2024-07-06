#!/usr/bin/python3

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    postdata = urllib.parse.urlencode(email)
    data = postdata.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        print("Your email is: {}".format(email['email']))
