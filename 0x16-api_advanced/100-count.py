#!/usr/bin/python3
"""Get frequency of keywords in posts in a Subreddit"""


import collections
import io
import json
import requests
import urllib.parse


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Get frequency of keywords in posts in a Subreddit"""

    path = 'https://www.reddit.com'
    path += '/r/' + urllib.parse.quote(subreddit, safe='') + '/hot.json'
    path += '?raw_json=1'
    if after is not None:
        path += '&after=' + urllib.parse.quote_plus(after)
        path += '&count=' + str(len(hot_list))
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'python:hbtn701t3:1 (by /u/SamHermesBoots)'
    }
    response = requests.get(path, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    posts = response.json()
    hot_list.extend(p['data']['title'] for p in posts['data']['children'])
    after = posts['data']['after']
    if after is None:
        word_list = collections.Counter(word_list)
        counter = collections.Counter(
            word
            for title in hot_list for word in title.lower().split()
        )
        print('\n'.join(
            '{}: {}'.format(word, count)
            for word, count in sorted((
                (word, counter[word.lower()] * words)
                for word, words in word_list.items()
                if counter[word.lower()] > 0
            ), key=lambda pair: (-pair[1], pair[0]))
        ))
        return
    return count_words(subreddit, word_list, hot_list, after)
