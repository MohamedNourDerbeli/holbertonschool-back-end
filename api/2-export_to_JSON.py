#!/usr/bin/python3
"""
This script will use the REST API to return information
about a given employee's TODO list progress.
"""
import json
import requests
import sys


def TODO_REQUESTS(ID):
    """
    extend your Python script to export data in the json format
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    ).json()
    user = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{ID}"
    ).json()
    data = {

        ID: [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos
        ]
    }
    with open(f"{ID}.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    ID = sys.argv[1]
    TODO_REQUESTS(ID)
