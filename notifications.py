import json


def loadData():
    # load the data from the file
    with open('campsitesAvailability.json') as json_data:
        jsonData = json.load(json_data)
    return jsonData

# find all sites that are available


def findAvailableSites(jsonData):
    availableSites = []
    # to-do: expand checking so that it checks based on variable
    for i in jsonData:
        #print(i['day'] == '4')
        # if (i['day'] == '4' or i['day'] == '5') and (i['month'] == 'Sep') and (i['data']['available']):
        if (i['data']['available']):
            availableSites.append(i)

    return availableSites


def findUsableSites(availableSites):
    usableSites = []
    for i in availableSites:
        if (i['data']['site'] <= '642' or i['data']['site'] == '654'):
            usableSites.append(i)
    return usableSites


def formatMessageHTML(usableSites):
    message = "Available campsites for Winter Camping: <br><br>"

    for i in usableSites:
        listing = i['month'] + " " + i['day'] + ", " + i['year']
        listing += " | Site " + i['data']['site']
        message += listing + "<br>"

    print(message)

    return message


def formatMessage(usableSites):
    message = "Available campsites for Winter Camping: \n\n"

    for i in usableSites:
        listing = i['month'] + " " + i['day'] + ", " + i['year']
        listing += " | Site " + i['data']['site']
        message += listing + "\n"

    print(message)

    return message


def getMessage():
    jsonData = loadData()
    availableSites = findAvailableSites(jsonData)
    #usableSites = findUsableSites(availableSites)
    return formatMessage(availableSites)


def getMessageHTML():
    jsonData = loadData()
    availableSites = findAvailableSites(jsonData)
    #usableSites = findUsableSites(availableSites)
    return formatMessageHTML(availableSites)
