"""
To solve this mission you must use the SendGrid API Key
(this video will explain how to create your own API Key).
Check out these Python examples.

It all starts with your first email. Let’s try to send one.

Your mission is to create a function that sends a welcome email to a user.
The function gets two arguments: email and the name of the user.

Subject of the email should be "Welcome" and body simply
"Hi {name}" ({name} should be replaced by a user's name)

Input: Two arguments: email and a username.

Output: None. You should send an email. You don’t need to return anything.
"""

## Examples:
## https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail_example.py#L9

import os
import sendgrid
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import Content

API_KEY = os.environ.get('SENDGRID_API_KEY')
API_KEY2 = 'abc'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(API_KEY)

def send_email(email, name):
    mail_txt = Content('text/plain', BODY.replace('{}',name))
    message = Mail(
        from_email=email,
        to_emails=email,
        subject=SUBJECT)
    message.add_content(mail_txt)
    response = sg.send(message)
    #print(response.status_code)
    #print(response.body)
    #print(response.headers)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('grzegorz.wieczerzak@gmail.com', 'Some Body')
    print('Done')
