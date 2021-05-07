import requests
import json
import datetime
from notifications import getMessage

webhook_url = 'https://discord.com/api/webhooks/840259728101212234/TvsBU0l78wvbS5ydbsynItdRxlDS4SdstXnxPCAC--uUEBea24ZDK3Bp-vkRtuVkeLvm'

time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
content = "**\*\* LATEST UPDATE as of " + \
    time + "\*\***\n" + getMessage() + "\n"
data = {'content': content}


def sendDiscordUpdate():
    r = requests.post(webhook_url, data=json.dumps(
        data), headers={'Content-Type': 'application/json'})
    print(r)
