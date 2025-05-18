from flask import Flask

app = Flask(__name__)

from WorkingWithHTML.app import routes
