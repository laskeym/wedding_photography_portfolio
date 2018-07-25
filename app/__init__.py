from flask import Flask
from config import Config

import logging

from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

# Logging
handler = logging.FileHandler('/var/log/lexispringer_log/app.log')
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)

# Flask Mail
mail = Mail(app)

from app.views import views