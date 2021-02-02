#!/usr/bin/python3
"""Makes a request to an API"""
import requests
import sys


if __name__ == '__main__':
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(sys.argv[1]))
    name = emp.json().get('name')
    user = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(sys.argv[1]))
    jdaughters = user.json()
    finished = 0
    count = 0
    for i in jdaughters:
        count += 1
        if i.get('completed'):
            finished += 1
    print('Employee {} is done with tasks({}/{}):'.
          format(name, count, finished))
    for i in jdaughters:
        if i.get('completed'):
            print('\t {}'.format(i.get('title')))
