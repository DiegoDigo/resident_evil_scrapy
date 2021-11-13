from pymongo import MongoClient


def get_database():
    connection_args = {
        "zlibCompressionLevel": 7,
        "compressors": "zlib"
    }
    client = MongoClient('mongodb://root:MongoDB2019!@localhost:27017/', **connection_args)
    return client['scrap_resident_evil']


DB_GAME = get_database().Game
DB_CHARACTER = get_database().Character
DB_CREATURE = get_database().Creature
