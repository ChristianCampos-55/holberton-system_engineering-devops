#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Gets ammount of subs """
    url = 'https://www.reddit.com/r/subreddit/about.json'
    req_headers = {'user-agent': 'chris'}
    try:
        reddit_req = requests.get(url, headers=req_headers,
                                  allow_redirects=False)
        return reddit_req.json().get('data').get('subscribers')
    except Exception:
        return 0
