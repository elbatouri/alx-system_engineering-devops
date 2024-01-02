#!/usr/bin/python3
"""
export data in the CSV format

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""


import sys
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    todos_response = requests.get(f"{url}todos", params={"userId": user_id})
    todos = todos_response.json()
    csv_filename = f"{employee_id}.csv"
    username = user.get("username")

    with open(csv_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, todo.get("completed"), todo.get("title")]
            )for todo in todos]
