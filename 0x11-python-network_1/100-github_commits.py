#!/usr/bin/python3

"""
fetch the last 10 commits
parse the sha parse the committer name
"""

if __name__ == '__main__':
    import requests
    import sys

    r = sys.argv[1]
    o = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(o, r)
    re = requests.get(url)
    if re.status_code == 200:
        r_json = re.json()
        limit = min(10, len(r_json))
        for i in range(limit):
            sha = r_json[i]['sha']
            author = r_json[i]['commit']['author']['name']
            print('{}: {}'.format(sha, author))
