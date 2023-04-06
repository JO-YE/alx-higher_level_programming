#!/usr/bin/python3
'''script that takes 2 arguments to print 10 commit for a repo
'''
import sys
import requests


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    req = requests.get(url)

    commit_h = req.json()
    for commit in commit_h[0:10]:
        sha = commit.get("sha")
        commiter = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, commiter))
