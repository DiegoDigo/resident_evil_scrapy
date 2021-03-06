from dataclasses import asdict
from bson.objectid import ObjectId
from src.core.infra import sql
from src.data.command.output.response_models import GameResponse

_DB = sql.DB_GAME


def _add_game_response(character):
    """Metodo para gerar a respota de games"""
    return asdict(
        GameResponse(character.get('_id'),
                     character.get('name'),
                     character.get('image'),
                     character.get('synopsis'),
                     character.get('release')))


def get_all():
    """Metodo para buscar todos os character com seus gamoes"""
    return [_add_game_response(character) for character in _DB.find()]


def get_by_id(id: str) -> dict:
    filter = {"_id": {"$eq": ObjectId(id)}}
    game = _DB.find_one(filter)
    return _add_game_response(game)
