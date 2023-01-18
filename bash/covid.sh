#!/bin/bash
# This script downloads covid data and displays it

# Gets the data from the api
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)


#set positive cases
POSITIVE=$(echo $DATA | jq '.[0].positive')
# set negative cases
NEGATIVE=$(echo $DATA | jq '.[0].negative')
# set pending cases
PENDING=$(echo $DATA | jq '.[0].pending')
# set Currently in ICU
ICU=$(echo $DATA | jq '.[0].inIcuCurrently')
# set deaths
DEATH=$(echo $DATA | jq '.[0].death')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases
$NEGATIVE negative COVID cases,
$PENDING pending COVID cases,
$ICU people currently in the ICU due to COVID,
$DEATH total deaths attributed to COVID."

