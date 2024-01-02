#!/usr/bin/python3
"""
export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
File name must be: USER_ID.json
"""

import json
import requests
import sys

if __main__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "user/{}".format(user_id)).json()
    username = user.get("username")
    todos_response = requests.get(f"{url}todos", params={"userId": user_id})
    todos = todos_response.json()
    json_filename = f"{user_id}.json"

    # write data to json file
    with open(json_filename, "w") as json_file:
        json.dump({user_id: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
            } for todo in todos]}, jsonfile)
