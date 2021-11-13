from dataclasses import asdict

from src.core.infra import sql
from src.data.command.output.response import GameResponse

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
