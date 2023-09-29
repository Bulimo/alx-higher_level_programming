#!/usr/bin/python3
"""
Module 100-github_commits
scrit that lists 10 commits (from the most recent to oldest)
of the given repository and user
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    repo_name = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo_name)

    res = requests.get(url)
    commit_data = res.json()

    for commit in commit_data[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
