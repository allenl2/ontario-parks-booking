from bs4 import BeautifulSoup
import re
import json
import logging


def parseData(table) -> list:
    """ Parses HTML to extract individual campsite date/location entries

    Parameters:
        table (str): HTML table from webpage

    Returns:
        list: list of available campsites in dict objects
    """

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

            siteNum = campsiteInfo[0].strip().replace(',', '')
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
                    "available": isAvailable
                }
            }
            campsitesArr.append(campsiteData)

    logging.info("Data parsed")
    return campsitesArr


def saveData(data):
    """ Saves provided date to json file

    Parameters:
        data (List): a list of indiviudal available sites

    Returns:
        n/a
    """

    # save data to a file
    with open('campsitesAvailability.json', 'w') as outfile:
        json.dump(data, outfile)
        logging.info("Data saved")

# to-do: format json using logic so dates are grouped together
