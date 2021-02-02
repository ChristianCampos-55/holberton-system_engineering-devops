#!/usr/bin/python3
"""Makes a request to an API"""
import json
import requests
import sys


if __name__ == '__main__':
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(sys.argv[1]))
    usr_name = emp.json().get('username')
    user = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(sys.argv[1]))
    jdaughters = user.json()
    exp = {}
    exp['{}'.format(sys.argv[1])] = []
    for i in jdaughters:
        exp['{}'.format(sys.argv[1])].append({
            'task': i.get('title'),
            'completed': i.get('completed'),
            'username': usr_name
        })
    with open('{}.json'.format(sys.argv[1]), 'w') as file:
        json.dump(exp, file)
