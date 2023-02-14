# Get the list of you courses from Canvas API

# Must authenticate
COURSES = $(curl "https://canvas.instructure.com/api/v1/users/self/favorites/courses \
    -H 'Authorization: Bearer <ACCESS_TOKEN>'")

    # Replace <ACCESS_TOKEN> with your access token from Canvas

#Get how many courses there are and tell user
COURSENUMBER=$(echo $COURSES | jq '. | length')
echo "There are $COURSENUMBER in your favorites. They are: "

# Loops through all the courses in the favorites and displays the name (loop found on https://www.geeksforgeeks.org/bash-scripting-for-loop/)
for n in ${COURSES[@]}; 
do
    COURSENAME=$(echo $n | jq '.name')
    echo $COURSENAME

done