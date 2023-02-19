import requests
import json

# Replace <ACCESS_TOKEN> with the token you got from Canvas
auth = {'Authorization': 'Bearer <ACCESS_TOKEN>'}
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