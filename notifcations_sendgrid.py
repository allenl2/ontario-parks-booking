import os
import datetime
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from notifications import getMessage

load_dotenv('.env')


def sendEmailUpdate():
    time = datetime.datetime.now().strftime("%m/%d/%Y")
    availability = getMessage()
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
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


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
