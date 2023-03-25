import requests
import json
import yaml

# Get the config out of the yaml file
# read from a YAML file
with open('project2/config.yaml', 'r') as config_file:
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
    course_name = course['name']
    print(course_name)