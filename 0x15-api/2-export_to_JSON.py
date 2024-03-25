#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format."""

import json
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

    dictionary = {emp_Id: []}
    for task in tasks:
        dictionary[emp_Id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": emp_Name
        })
    with open('{}.json'.format(emp_Id), 'w') as filename:
        json.dump(dictionary, filename, indent=4)
