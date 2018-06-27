from flask import Flask
from config import Config

from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

# Flask Mail
mail = Mail(app)

from app.views import views