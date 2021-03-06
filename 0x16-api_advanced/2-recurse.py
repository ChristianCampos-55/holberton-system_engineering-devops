#!/usr/bin/python3
""" Queries the Reddit API and prints titles of first 10 posts """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Prints titles of first 10 posts listed """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    req_headers = {'User-agent': 'chris'}
    try:
        reddit_req = requests.get(url, headers=req_headers,
                                  allow_redirects=False)
        if after is None:
            return hot_list
        req_json = reddit_req.json()
        for child in req_json['data']['children']:
            hot_list.append(child)
        after = req_json['data']['after']
        return recurse(subreddit, hot_list, after)
    except Exception:
        return None
