#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format"""
import json
import requests


def fetch_todo_list(url):
    """Fetches to-do list information for all users."""
    users_response = requests.get(url + "users")
    users = users_response.json()

    todo_data = {}
    for user in users:
        user_id = user["id"]
        todos_response = requests.get(url + f"todos?userId={user_id}")
        todos = todos_response.json()

        user_todos = []
        for todo in todos:
            user_todos.append({
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            })

        todo_data[user_id] = user_todos

    return todo_data


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    todo_data = fetch_todo_list(base_url)

    with open("todo_all_employees.json", "w") as file:
        json.dump(todo_data, file, indent=4)
