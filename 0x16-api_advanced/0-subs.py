#!/usr/bin/python3
"""
"""

import requests


def number_of_subscribers(subreddit):
    url=requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    headers = {'User-Agent': 'elbarabi'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
