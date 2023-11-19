from flask import Flask
from flask_cors import CORS
import os

from src.routes.users import users
from src.routes.games import games
from src.routes.bought import bought

app = Flask(__name__)

CORS(app)

app.register_blueprint(users, url_prefix="/v1")
app.register_blueprint(games, url_prefix="/v1")
app.register_blueprint(bought, url_prefix="/v1")

app.run(debug=True, port=8080)
