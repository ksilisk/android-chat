from app import make_app
from database import DatabaseClient
from data_validator import Validator

DB_URL = 'localhost'
DB_NAME = 'test'
DB_PORT = 27017

db = DatabaseClient(DB_URL, DB_NAME, DB_PORT)
db.create_indexes()
validator = Validator()
app = make_app(validator, db)

if __name__ == "__main__":
    app.run()
