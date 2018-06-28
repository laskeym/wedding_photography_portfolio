from threading import Thread
from app import app, mail 

from flask import render_template
from flask_mail import Message

from config import Config
from .decorators import async


@async
def send_async_email(app, msg):
  with app.app_context():
    mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
  msg = Message(subject, sender=sender, recipients=recipients, reply_to=sender)
  msg.body = text_body
  msg.html = html_body
  send_async_email(app, msg)

def contact_submit(first_name, last_name, email_addr, date):
  subject = 'LSP: {first_name} has requested an appointment!'.format(first_name=first_name)
  send_email(subject, email_addr, [Config.MAIL_USERNAME], '',
             render_template('email/contact_self_email.html', first_name=first_name, last_name=last_name, date=date))