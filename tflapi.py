import requests
import json

print('hello,world!')

# setting the routes and bus stop so it can be changed more dynamically
route = '262,376'
stop = '490005505W'

# api request, made into a function for reusability
def findtime(routes, stopID):
    datump = requests.get('https://api.tfl.gov.uk/Line/{}/Arrivals/{}'.format
    (routes, stopID))
    return json.loads(datump.text)
# function that creates an array of bus IDs and time to stops, in seconds
def makedat():
    # create a json thing using the findtime function
    jsonlist = findtime(route, stop)
    # empty array to append buses and times to
    busarray = []
    # go through each entry in the json thing, and add a tuple to the array
    # the tuple consists of the bus route, and the minutes-to-stop
    for i in jsonlist:
        x = i['timeToStation'] / 60
        busarray.append((i['lineId'], int(x)))
    # function sorts that list by bus, then minutes-to-stop, and returns the
    # sorted array.
    busarray = sorted(busarray, reverse=False)
    return busarray

# as a test, print an example array
print(makedat())
