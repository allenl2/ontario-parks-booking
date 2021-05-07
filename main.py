from clicker import retriveTableData
from parsedata import saveData, parseData
from notifications_twilio import sendMessage
from notifications_discord import sendDiscordUpdate
from notifcations_sendgrid import sendEmailUpdate
import time

# retrive the data from website, parse, save to file
table = retriveTableData()
siteData = parseData(table)
saveData(siteData)

# send relevant notifications
# sendMessage()
sendDiscordUpdate()
sendEmailUpdate()
