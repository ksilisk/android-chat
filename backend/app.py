from werkzeug.security import generate_password_hash, check_password_hash
from data_validator import Validator
from pymongo.database import Database
from flask import Flask


def make_app(valid: Validator, db: Database):
    app = Flask('TestAPP')
    return app
