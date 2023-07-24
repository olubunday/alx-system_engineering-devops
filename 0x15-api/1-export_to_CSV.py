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
    with open(sys.argv[1] + '.csv', 'wt', newline='') as file:
        file = csv.writer(file, quoting=csv.QUOTE_ALL)
        row = [sys.argv[1], user.get('username'), '', '']
        for task in tasks:
            row[2] = str(task.get('completed'))
            row[3] = task.get('title')
            file.writerow(row)
