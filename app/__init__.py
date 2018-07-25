from flask import Flask
from config import Config

import logging

from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

# Logging
handler = logging.FileHandler('/home/alexis/lexispringer_flask/log/app.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setLevel(logging.ERROR)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Flask Mail
mail = Mail(app)

from app.views import views
