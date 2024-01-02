#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # Define the base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user and to-do list data using the provided employee ID
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Extract completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the results in the specified format
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the titles of completed tasks
    [print("\t {}".format(c)) for c in completed]
