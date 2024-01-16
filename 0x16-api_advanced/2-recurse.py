#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles 
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
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])

            for child in children:
                hot_list.append(child['data']['title'])

            after = data.get('after')

            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
