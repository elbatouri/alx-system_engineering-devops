#!/usr/bin/env python3
"""
queries the Reddit API and returns a list containing the titles 
of all hot articles for a given subreddit. If no results are found 
for the given subreddit, the function should return None.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    
    user_agent = 'elbatouri/1.0'
    client_id = 'WqSQ8WwNC9Y6ixCB1Gx9sA'
    headers = {'User-Agent': user_agent,
               'Authorization': f'Client-ID {client_id}'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    params = {'limit': 100, 'after': after}

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
