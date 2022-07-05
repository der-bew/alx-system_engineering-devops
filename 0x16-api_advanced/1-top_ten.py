#!/usr/bin/python3
"""
1. Top Ten
"""
import requests


def top_ten(subreddit):
    """ Print the titles of the 10 hot post for a given subreddit """
    api_url = 'https://www.reddit.com'

    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    res = requests.get(f'{api_url}/r/{subreddit}/hot.json?limit=10',
                       headers=headers, allow_redirects=False)
    if res.status_code == 200:
        for hot in res.json().get('data').get('children'):
            print(hot.get('data').get('title'))
    else:
        print(None)
