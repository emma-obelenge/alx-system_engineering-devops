#!/usr/bin/python3
"""Program that that export API data to JSON file format"""
import json
import requests
import sys

if __name__ == '__main__':
    try:
        # Attempting to convert user argument to an int value
        employee_id = int(sys.argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    usr_uri = '{}/users/{}'.format(api_url, employee_id)
    todo_uri = '{}/todos'.format(usr_uri)

    # file name saving format
    file_name = "{}.json".format(employee_id)

    # User Response
    user_resp = requests.get(usr_uri).json()

    # User TODO Response
    todo_resp = requests.get(todo_uri).json()

    # List containig all task of the user
    user_tasks = []
    for elem in todo_resp:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': user_resp.get('username')
        }

        user_tasks.append(data)

    # Create the new file for the user to save the information
    # Filename example: `{user_id}.json`
    with open(file_name, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps({employee_id: user_tasks}))
