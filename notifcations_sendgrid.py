import os
import datetime
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from notifications import getMessageHTML
import logging

load_dotenv('.env')

TEMPLATE_ID = 'd-31f56eb3d5e14c6884e681c5d3e9919d'


def sendEmailUpdate():
    time = datetime.datetime.now().strftime("%m/%d/%Y")
    availability = getMessageHTML()
    content = generateHTML(time, availability)

    # send email using SendGrid
    message = Mail(
        from_email='allenl.dev@gmail.com',
        to_emails='2002allenliu@gmail.com',
        subject='Campsites Availability Update: {time}'.format(time=time),
        html_content=content)
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_TOKEN'))
        response = sg.send(message)
        logging.info(response.status_code)
    except Exception as e:
        logging.error(e.message)


def sendDynamicEmailUpdate() -> int:
    """ Send a dynamic email to a list of email addresses

    Parameters:
        n/a

    Returns:
        int: API response code
    """
    time = datetime.datetime.now().strftime("%m/%d/%Y")
    availability = getMessageHTML()

    # create Mail object and populate
    message = Mail(
        from_email='allenl.dev@gmail.com',
        to_emails='2002allenliu@gmail.com'
    )
    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        'subject': 'Campsites Availability Update: {time}'.format(time=time),
        'date': time,
        'availability': availability,
    }
    message.template_id = TEMPLATE_ID
    # create our sendgrid client object, pass it our key, then send and return our response objects
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_TOKEN'))
        response = sg.send(message)
        code, body, headers = response.status_code, response.body, response.headers
        logging.info(f"Email sent. Response code: {code}")
    except Exception as e:
        logging.error("Error: {0}".format(e))
    return str(response.status_code)


def generateHTML(time, availability):
    content = """
    <div style="background-color: #155414; border-radius: 15px; padding: 20px">
        <h1 style="color: white; font-size: 28px; font-family: Calibri; font-weight: bold">Daily Campsite Availability</h1>
        <h2 style="color: white; font-size: 20px; font-family: Calibri; font-style:italic">Last checked on {time}</h2>    
    </div>
    <br>
    <div style="border: 5px solid #13439c; border-radius: 15px; padding: 20px">
        <p style="font-size: 20px; font-family: Calibri"> {availability}</p>
    </div>
    <br>
    <form action="https://reservations.ontarioparks.com/">
        <input type="submit" value="Go to Booking Site" style="background-color: #13439c; border: 0px; border-radius: 15px; font-size: 20px; font-family: Calibri; color: white; padding: 20px; display: block; margin-left: auto; margin-right: auto; "/>
    </form>
    """.format(time=time, availability=availability)

    return content
