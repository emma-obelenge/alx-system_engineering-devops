#!/usr/bin/python3
"""Program that that export API data to JSON file format"""
import json
import requests
import sys

def extract_employee_tasks(response, employee):
    """
    Extract all the employee tasks
    """
    # Creates a list to store all the tasks of the employee
    employee_tasks = []

    # Find the tasks that belongs to employee passed into func
    for task in response:
        if task.get('userId') == employee.get('id'):
            task_data = {
                'username': employee.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
            }

            employee_tasks.append(task_data)

    # Returns the list of tasks
    return employee_tasks

if __name__ == '__main__':
    # formating names to API url's, uri's, and filename
    api_url = 'https://jsonplaceholder.typicode.com'
    usr_uri = '{}/users'.format(api_url)
    todo_uri = '{}/todos'.format(api_url)

    # file name saving format
    file_name = "todo_all_employees.json"

    # User Response
    user_resp = requests.get(usr_uri).json()

    # User TODO Response
    todo_resp = requests.get(todo_uri).json()

    # List containig all task of the user
    user_tasks = {}

    for user in user_resp:
        id_retrieved = user.get('id')
        username_retrieved = user.get('username')

        tasks = extract_employee_tasks(todo_resp, {
            'id': id_retrieved,
            'username': username_retrieved
        })

        # Inserting the list of all task of current employee
        # Into a dictionary that stores all the employees with their tasks.
        user_tasks[id_retrieved] = tasks

        # Creeate the new file with collected information
        # Filename example: 'todo_all_employees.json'
        with open(file_name, 'w', encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(user_tasks))
