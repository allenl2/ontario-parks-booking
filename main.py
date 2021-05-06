from clicker import retriveTableData
from parsedata import saveData, parseData
from notifications_sender import sendMessage
import time

# retrive the data from website, parse, save to file
table = retriveTableData()
siteData = parseData(table)
saveData(siteData)

# send text message
sendMessage()
