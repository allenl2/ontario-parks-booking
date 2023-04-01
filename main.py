from clicker import retriveTableData, navigateSite
from parsedata import saveData, parseData
from notifications_twilio import sendMessage
from notifications_discord import sendDiscordUpdate
from notifcations_sendgrid import sendEmailUpdate, sendDynamicEmailUpdate
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # retrive the data from website
    browser = navigateSite()
    table = retriveTableData(browser)
    browser.close()

    # parse and save data
    siteData = parseData(table)
    saveData(siteData)

    # send relevant notifications
    # sendMessage()
    # sendDiscordUpdate()
    # sendEmailUpdate()
    sendDynamicEmailUpdate()
