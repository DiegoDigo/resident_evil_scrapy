from pymongo import MongoClient


def get_database():
    client = MongoClient('mongodb://root:MongoDB2019!@localhost:27017/')
    return client['scrap_resident_evil']


DB_GAME = get_database().Game
DB_CHARACTER = get_database().Character
