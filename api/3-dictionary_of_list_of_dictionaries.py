#!/usr/bin/python3
"""
This script will use the REST API to return information
about a given employee's TODO list progress.
"""
import json
import requests
import sys


def TODO_REQUESTS():
    """
    extend your Python script to export data in the JSON format
    """
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users"
    ).json()

    data = [
        {
            user["id"]: [
                {
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"],
                }
                for task in todos
            ]
        }
        for user in user
    ]
    with open(f"test.json", "w") as jsonfile:
        json.dump(data[0], jsonfile)


if __name__ == "__main__":
    TODO_REQUESTS()
