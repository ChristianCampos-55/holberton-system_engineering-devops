#!/usr/bin/python3
""" Queries the Reddit API and prints titles of first 10 posts """
import requests


def top_ten(subreddit):
    """ Prints titles of first 10 posts listed """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req_headers = {'user-agent': 'chris'}
    try:
        reddit_req = requests.get(url, headers=req_headers,
                                  allow_redirects=False)
        req_json = reddit_req.json()
        for title in req_json['data']['children']:
            print(title['data']['title'])
    except Exception:
        print('None')
