from bs4 import BeautifulSoup
import re
import json


def parseData(table):
    # getting the data from the website
    content = BeautifulSoup(table, "html.parser")
    box = content.find('td')

    campsitesArr = []

    # for each listing, get the text description and parse it into an object
    for box in content.findAll('td'):
        currListing = box.get('aria-label')

        if isinstance(currListing, str):
            responseSplit = re.split('\n', currListing)
            campsiteInfo = re.split('-', responseSplit[0])

            print(responseSplit)

            siteNum = campsiteInfo[0].strip()
            siteName = campsiteInfo[1].strip().replace(',', '')
            isAvailable = True if responseSplit[3].strip(
            ) == 'Available' else False

            dateSplit = responseSplit[1].strip().split(',')
            weekday = dateSplit[0]
            year = dateSplit[2].strip()
            day = re.findall('[0-9]+', dateSplit[1])[0]
            month = re.findall('[A-z]+', dateSplit[1])[0]

            campsiteData = {
                "year": year,
                "month": month,
                "day": day,
                "weekday": weekday,
                "data": {
                    "site": siteNum,
                    "name": siteName,
                    "available": isAvailable
                }
            }
            campsitesArr.append(campsiteData)

    print("Data parsed")
    return campsitesArr


def saveData(data):
    # save data to a file
    with open('campsitesAvailability.json', 'w') as outfile:
        json.dump(data, outfile)
        print("Data saved")

# to-do: format json using logic so dates are grouped together
