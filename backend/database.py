from pymongo import MongoClient
from pymongo.database import Database


class DatabaseClient(Database):

    def __init__(self, url: str, name: str, port: int):
        super().__init__(MongoClient(url, port), name)
        self.__db_name = name

    @property
    def db_name(self) -> str:
        return self.__db_name

    def create_indexes(self):
        pass
