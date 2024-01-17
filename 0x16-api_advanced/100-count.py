#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not)."""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    if word_counts is None:
        word_counts = Counter()

    user_agent = {'User-agent': 'elbatouri/1.0'}
    client_id = 'WqSQ8WwNC9Y6ixCB1Gx9sA'
    headers = {'User-Agent': user_agent['User-agent'],
               'Authorization': f'Client-ID {client_id}'}
    url = f'http://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}")
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                if f' {word} ' in f' {title} ':
                    word_counts[word] += 1

        after = data.get('after')

        if after is not None:
            return count_words(subreddit, word_list, after, word_counts)
        else:
            sorted_counts = sorted(word_counts.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f'{word.lower()}: {count}')
    except Exception as e:
        print(f"An error occurred: {e}")
