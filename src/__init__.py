# src/__init__.py

from flask import Flask

app = Flask(__name__)

import src.main
import src.model
import src.predict
