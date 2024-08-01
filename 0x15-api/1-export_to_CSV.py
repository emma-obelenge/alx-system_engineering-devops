#!/usr/bin/python3
"""Program that that export API data to csv format"""
import csv
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
    
    #file name saving format
    file_name = "{}.csv".format(employee_id)

    # User Response
    response = requests.get(usr_uri).json()

    # Getting the employee username
    emp_username = response.get('username')

    # User TODO Response
    response = requests.get(todo_uri).json()

    # Creating new file for saving user info
    with open(file_name, 'w', encoding='utf-8') as csvfile:
        save = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in response:
            # Completed or non-completed task
            status = elem.get('completed')

            # The task name
            title = elem.get('title')

            # Writing each result of API response in a row of a CSV file
            save.writerow([employee_id, emp_username, status, title])
