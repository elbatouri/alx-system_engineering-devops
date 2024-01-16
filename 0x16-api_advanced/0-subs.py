#!/usr/bin/python3
"""
This function queries Reddit API and retrieves the number of subscribers for a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Function to return the number of subscribers"""
    user = {'User-Agent': 'elbatouri'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user)

    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)

