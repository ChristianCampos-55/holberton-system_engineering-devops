#!/usr/bin/python3
"""Makes a request to an API"""
import csv
import requests
import sys


if __name__ == '__main__':
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(sys.argv[1]))
    usr_name = emp.json().get('username')
    user = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(sys.argv[1]))
    jdaughters = user.json()
    with open('{}.csv'.format(sys.argv[1]), mode='w') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for i in jdaughters:
            writer.writerow([sys.argv[1], usr_name, i.get('completed'),
                             i.get('title')])
