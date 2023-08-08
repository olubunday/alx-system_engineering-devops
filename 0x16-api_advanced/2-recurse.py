#!/usr/bin/python3
"""Get all hot posts on a Subreddit"""


import http.client
import io
import json
import urllib.parse


def recurse(subreddit, hot_list=[], after=None, client=None):
    """Get all hot posts on a Subreddit"""

    path = '/r/' + urllib.parse.quote(subreddit, safe='') + '/hot.json'
    path += '?raw_json=1'
    if after is not None:
        path += '&after=' + urllib.parse.quote_plus(after)
        path += '&count=' + str(len(hot_list))
    if client is None:
        client = http.client.HTTPSConnection('www.reddit.com')
        client.connect()
    client.putrequest('GET', path)
    client.putheader('Connection', 'keep-alive')
    client.putheader('User-Agent', 'python:hbtn701t2:1 (by /u/SamHermesBoots)')
    client.endheaders()
    response = client.getresponse()
    if response.status != 200:
        client.close()
        return None
    posts = json.load(io.TextIOWrapper(response, encoding='UTF-8'))
    if response.getheader('Connection', 'close') == 'close':
        client.close()
        client = None
    hot_list.extend(p['data']['title'] for p in posts['data']['children'])
    if posts['data']['after'] is None:
        client.close()
        return hot_list
    return recurse(subreddit, hot_list, posts['data']['after'], client)
