import requests
import json

print('hello,world!')

# setting the routes and bus stop so it can be changed more dynamically
route = '262,376'
stop = '490005505W'

# api request, made into a function for reusability
def findtime(routes, stopID):
    datump = requests.get('https://api.tfl.gov.uk/Line/{}/Arrivals/{}'.format(routes, stopID))
    return json.loads(datump.text)
# function that creates an array of bus IDs and time to stops, in seconds
def makedat():

    jsonlist = findtime(route, stop)

    busarray = []

    for i in jsonlist:
        print(i['lineId'],i['vehicleId'], i['timeToStation'])
        x = i['timeToStation'] / 60
        if x <= 1:
            print(i['lineID'], ' Due')
        else:
            print(i['lineID'], ' ', int(x), ' Minutes')

makedat()
