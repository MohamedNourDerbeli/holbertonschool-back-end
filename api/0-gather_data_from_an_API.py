#!/usr/bin/python3
"""
This script will use the REST API to return information
about a given employee's TODO list progress.
"""
import requests
import urllib.request
import sys
import json


def TODO(ID):
    """
    This function will return the TODO list progress of a given employee
    """
    # Get the TODO list of the employee
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    request_todos_url = urllib.request.urlopen(todos_url)
    todos_data = request_todos_url.read().decode("utf-8")
    todos = json.loads(todos_data)
    done_tasks = 0
    total_tasks = len(todos)
    # Get the number of done tasks
    for task in todos:
        if task["completed"] is True:
            done_tasks += 1

    # Get the name of the employee
    users_url = f"https://jsonplaceholder.typicode.com/users/{ID}"
    request_users_url = urllib.request.urlopen(users_url)
    users_data = request_users_url.read().decode("utf-8")
    users = json.loads(users_data)
    employee_name = users["name"]
    print(
        f"Employee {employee_name} is done with \
tasks({done_tasks}/{total_tasks}):"
    )
    # Print the title of the done tasks
    for task in todos:
        if task["completed"] is True:
            print(f"\t {task['title']}")


def TODO_REQUESTS(ID):
    """
    This functionis the same as the previous one but with a different
    way to get the data using requests
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    ).json()
    user_info = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{ID}"
    ).json()
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    print(
        f"Employee {user_info['name']} is done with tasks\
({len(completed_tasks)}/{len(todos)}):"
    )
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    ID = sys.argv[1]
    TODO(ID)
    # TODO_REQUESTS(ID)
