from decouple import config
import urllib.parse

from pymongo import MongoClient

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')


def get_database():
    username = urllib.parse.quote(USERNAME)
    password = urllib.parse.quote(PASSWORD)

    connection_args = {
        "zlibCompressionLevel": 7,
        "compressors": "zlib"
    }

    mongo_uri = f'mongodb+srv://{username}:{password}@residentevil.szct5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = MongoClient(mongo_uri, **connection_args)
    return client['resident_evil']


DB_APPEARANCES = get_database().Appearances
DB_CHARACTER = get_database().Character
DB_CREATURE = get_database().Creature
DB_GAME = get_database().Game


def drop_collection(db):
    db.drop()
