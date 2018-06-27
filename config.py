import os


# Administrator List
ADMINS = ['laskeymark0413@gmail.com']

class Config(object):
  # Secret Key
  SECRET_KEY = os.environ.get('SECRET_KEY')

  # Email Server
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')