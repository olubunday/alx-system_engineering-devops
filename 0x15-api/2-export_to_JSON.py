#!/usr/bin/python3
"""Synthesize data from an HTTP API"""


import csv
import json
import sys
import urllib.request


if __name__ == '__main__':
    request = urllib.request.Request(
        'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    )
    with urllib.request.urlopen(request) as response:
        user = json.loads(response.read().decode())
    request = urllib.request.Request(
        'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    )
    with urllib.request.urlopen(request) as response:
        tasks = json.loads(response.read().decode())
    with open(sys.argv[1] + '.json', 'wt') as file:
        json.dump({sys.argv[1]: [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user.get('username')
            } for task in tasks
        ]}, file)
