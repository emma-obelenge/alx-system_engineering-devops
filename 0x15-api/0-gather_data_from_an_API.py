#!/usr/bin/python3
"""Program that uses Employee ID to return information about their TODO list"""
import requests
import sys

if __name__ == '__main__':
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        exit()
    api_url = 'https://jsonplaceholder.typicode.com'
    usr_uri = '{}/users/{}'.format(api_url, employee_id)
    todo_uri = '{}/todos'.format(usr_uri)

    # User Response
    response = requests.get(usr_uri).json()

    # Name of employee
    employee_name = response.get('name')

    # User TODO Response
    response = requests.get(todo_uri).json()

    # Total num of tasks, both completed and non-completed
    total = len(response)

    # Number of incomplete tasks
    incomplete = sum([elem['completed'] is False for elem in response])

    # Number of completed tasks
    complete = total - incomplete

    # Formatting the expected output
    str = "Employee {} is done with tasks({}/{}):"
    print(str.format(employee_name, complete, total))

    # Printing completed tasks
    for elem in response:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
"""
def employee_info(emp_id):
    url = f'https://jsonplaceholder.typicode.com/todos/{emp_id}'

    with urllib.request.urlopen(url) as response:
        response_data = response.read().decode()
        data = json.loads(response_data)
        return (data)

strings = employee_info(employee_id)
print(f"type is {type(strings)} and data is: \n{strings}")
"""
