#!/usr/bin/env python3
"""
return ueries the Reddit API and
prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    user_agent = 'elbatouri/1.0'
    client_id = 'WqSQ8WwNC9Y6ixCB1Gx9sA'
    headers = {'User-Agent': user_agent,
               'Authorization': f'Client-ID {client_id}'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
