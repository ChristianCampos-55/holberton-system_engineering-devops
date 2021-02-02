#!/usr/bin/python3
"""Makes a request to an API"""
import json
import requests
import sys


if __name__ == '__main__':
    ids = set()
    user = requests.get('https://jsonplaceholder.typicode.com/posts')
    jdaughters = user.json()
    for i in jdaughters:
        ids.add(i.get('userId'))
    exp = {}
    for i in ids:
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(i))
        usr_name = user.json().get('username')
        usr_todos = requests.get('https://jsonplaceholder.typicode.com/' +
                            'todos?userId={}'.format(i))
        jdaughters = usr_todos.json()

        exp['{}'.format(i)] = []
        for j in jdaughters:
            exp['{}'.format(i)].append({
                'username': usr_name,
                'task': j.get('title'),
                'completed': j.get('completed')
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump({int(x): exp[x] for x in exp.keys()},
                  file, sort_keys=True)
