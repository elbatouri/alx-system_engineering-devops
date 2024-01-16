#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not)."""


import requests
from collections import Counter


def count_words(subreddit, word_list, found_list=None, after=None):
    if found_list is None:
        found_list = []

    user_agent = {'User-agent': 'elbatouri/1.0'}
    client_id = 'WqSQ8WwNC9Y6ixCB1Gx9sA'
    headers = {'User-Agent': user_agent['User-agent'],
               'Authorization': f'Client-ID {client_id}'}
    url = f'http://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    posts = requests.get(url, headers=headers)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)

        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            word_counts = Counter(found_list)
            for word, count in word_counts.most_common():
                print(f'{word}: {count}')
    else:
        return
