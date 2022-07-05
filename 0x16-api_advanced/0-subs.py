#!/usr/bin/python3
"""
0. How many subs?

"""
import requests


def number_of_subscribers(subreddit):
    """ Get a number of subscribers of a subreddit """
    api_url = 'https://www.reddit.com'

    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    res = requests.get(f'{api_url}/r/{subreddit}/about.json',
                       headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    return 0
