#!/usr/bin/python3
"""
queries redditapi and return subscribers number in subbreddit
"""
import requests


def number_of_subscribers(subreddit):
    user_agent = 'elbatouri/1.0'
    client_id = 'WqSQ8WwNC9Y6ixCB1Gx9sA'
    headers = {'User-Agent': user_agent,
               'Authorization': f'Client-ID {client_id}'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
