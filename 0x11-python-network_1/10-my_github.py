#!/usr/bin/python3

"""
    Python Script Take Credentials and Dislay ID
"""
if __name__ == "__main__":
    import requests
    import sys

    u = sys.argv[1]
    password = sys.argv[2]
    h = {
        'Authorization': f'Bearer {password}'
        }

    r = requests.get('https://api.github.com/users/{}'.format(u), headers=h)
    if r.status_code == 200:
        r_json = r.json()
        print(r_json['id'])
    else:
        print('None')
