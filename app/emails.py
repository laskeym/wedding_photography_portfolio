from flask import render_template

from flask_mail import Message
from app import mail

from config import Config


def send_email(subject, sender, recipients, text_body, html_body):
  msg = Message(subject, sender=sender, recipients=recipients)
  msg.body = text_body
  msg.html = html_body
  mail.send(msg)

def contact_submit(first_name, last_name, email_addr, date):
  send_email('LSP: {first_name} has requested an appointment!'.format(first_name=first_name), email_addr, [Config.MAIL_USERNAME], '',
             render_template('email/contact_self_email.html', first_name=first_name, last_name=last_name, date=date))