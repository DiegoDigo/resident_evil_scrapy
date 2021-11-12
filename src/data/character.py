from pprint import pprint

from src.core import sql

_DB = sql.DB_CHARACTER


def get_all():
    stage_lookup = {
        "$lookup":
            {
                "from": "Game",
                "localField": "_id",
                "foreignField": "character_id",
                "as": "games"
            }
    }

    pipeline = [
        stage_lookup,
    ]

    teste = _DB.aggregate(pipeline)

