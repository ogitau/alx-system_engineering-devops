#!/usr/bin/python3
"""Extend the Python script to export data in the CSV format."""

import requests
from sys import argv


if __name__ == '__main__':
    emp_Id = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f"{baseUrl}/{emp_Id}"

    with requests.get(url) as response:
        emp_Name = response.json().get('username')

        todoUrl = f"{url}/todos"

        with requests.get(todoUrl) as response:
            tasks = response.json()

        with open('{}.csv'.format(emp_Id), 'w') as file:
            for task in tasks:
                file.write('"{}","{}","{}","{}"\n'
                       .format(emp_Id, emp_Name, task.get('completed'),
                               task.get('title')))
