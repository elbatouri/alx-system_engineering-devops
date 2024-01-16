#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    user_agent = 'elbatouri/1.0'
    client_id = 'WqSQ8WwNC9Y6ixCB1Gx9sA'
    headers = {'User-Agent': user_agent,
               'Authorization': f'Client-ID {client_id}'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False).json()

        if response.get('data') and response.get('data').get('children'):
            children = response['data']['children']

            for i in range(min(10, len(children))):
                print(children[i]['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
