#!/usr/bin/python3
""" Uses a REST API for a todo list of employee"""

import requests
from sys import argv


if __name__ == '__main__':
    emp_Id = argv[1]
    b_Url = "https://jsonplaceholder.typicode.com/users"
    url = f"{b_Url}/{emp_Id}"

    with requests.get(url) as response:
        emp_Name = response.json().get('name')

    todoUrl = f"{url}/todos"

    with requests.get(todoUrl) as response:
        tasks = response.json()

    tasks_done = [task for task in tasks if task.get('completed')]
    done = len(tasks_done)

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_Name, done, len(tasks)))
    for task in tasks_done:
        print("\t " + task.get("title"))
