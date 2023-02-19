# LAB 1

This lab is a python script that uses the Canvas API to list the names of the courses you have favorited

## SETUP

### STEP 1: Install requests library

To install the requests library type in the following command:

`pip install requests`

### STEP 2: Generate your Canvas Token

There are several ways to do this found here: [OAuth2 - Canvas LMS REST API Documentation (instructure.com)](https://canvas.instructure.com/doc/api/file.oauth.html#oauth2-flow-0)

I recommend doing it manually:

    1. Login into your uc.instructure.com account

    2. Go your user settings by clicking on your profile picture in the top left and clicking the word "Settings"

    3. Scroll down until you see "Approved integrations" and click on the "+ New Access Token" button

![1676385148623](image/README/1676385148623.png)

    4. Enter the Purpose and Expiration date for the token and click "Generate Token"

    5. Then copy the token that gets generated and close the modal

    6. In your script, replace <ACCESS_TOKEN> with your copied token and run the script
