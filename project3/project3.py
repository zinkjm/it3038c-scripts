import requests
import json
import yaml
import datetime


# Get the config out of the yaml file
# read from a YAML file
with open('project3/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
# get a value from the config
api_key = config['CANVAS']['API_KEY']

# Define auth variable to be used in response
auth = {'Authorization': 'Bearer %s' % api_key}
# Set the api url to get favorite courses
url = 'https://canvas.instructure.com/api/v1/users/self/favorites/courses'
# Send the request and set response to variable
response = requests.get(url, headers=auth)

# Format the json response to get all the courses
courses = json.loads(response.text)
#Set the total number of courses in your favorites
course_number = len(courses)
print("There are %s courses in your favorites. They are:" % course_number)

# Loop through all the courses to display each course name
for course in courses:
    # establish the id and the name of the course
    course_name = course['name']
    course_id = course['id']

    # Get the url for the webpage to see the grades
    grade_url = 'https://canvas.instructure.com/courses/%s/grades' % course_id

    print('Course: %s --- Grades found here: %s' % (course_name, grade_url))

# Gets user input to display assignments due for the favorite courses
print('Enter one of the following numbers to see assignments due: \n 1 Assignments due today \n 2 Assignments due this week \n 3 Assignments due this month ')
number = input()
# If the input isn't valid then prompt the user again
while number != "1" and number != "2" and number != "3":
        print('Error: Not a valid option.\n')
        print('Enter one of the following numbers to see assignments due: \n 1 Assignments due today \n 2 Assignments due this week \n 3 Assignments due this month')
        number = input()

# Set the due date range based on user input
if number == "1":
    today = datetime.datetime.now()
    due_date_range = [today, today]
elif number == "2":
    today = datetime.datetime.now()
    week_from_today = today + datetime.timedelta(days=7)
    due_date_range = [today, week_from_today]
elif number == "3":
    today = datetime.datetime.now()
    month_from_today = today + datetime.timedelta(days=30)
    due_date_range = [today, month_from_today]

# Loop through all the favorite courses and return the assignments due
for course in courses:
    # Get the assignments due
    assignment_url = 'https://canvas.instructure.com/api/v1/courses/%s/assignments' % course['id']
    assignments = requests.get(assignment_url, headers=auth)
    assignments_due = json.loads(assignments.text)

    # Only loop through assignments if there are assignments for that course with a due date
    if assignments_due:
        # Establish the number of assignments due
        number_assignments_due = 0

        # Loop through all the assignments and check if they are due within the specified range
        for assignment in assignments_due:
            due_date = assignment['due_at']
            if due_date:
                # format the due_date to match date range
                due_date = datetime.datetime.strptime(due_date, '%Y-%m-%dT%H:%M:%SZ')
                # Checks if the due date of the assignment is within the specified range
                if due_date_range[0] <= due_date <= due_date_range[1]:
                    # increase the number of assignments due for the entered range and print
                    number_assignments_due = number_assignments_due + 1
                    print('Course: %s --- Assignment: %s --- Due date: %s' % (course['name'], assignment['name'], assignment['due_at']))

        # if there aren't any assignments for the range due, display
        if number_assignments_due == 0:
            print('No assignments due for course %s' % course['name'])   

    # if there aren't any assignments for the course, then specify
    else:
        print('No assignments due for course: %s' % course['name'])


