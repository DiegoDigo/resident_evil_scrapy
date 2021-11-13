from dataclasses import asdict

from bson.objectid import ObjectId

from src.core.infra import sql
from src.data.command.output.response_models import CharacterResponse, AppearancesResponse

_DB = sql.DB_CHARACTER
_DB_APPEARANCES = sql.DB_APPEARANCES


def _get_games_response(games) -> list[AppearancesResponse]:
    """Metodo para gerar a respota de games"""
    return [asdict(AppearancesResponse(game.get('_id'), game.get('name'), game.get('year'))) for game in games]


def _add_character_response(character):
    """Metodo para gerar a respota de character"""
    return asdict(CharacterResponse(character.get('_id'), character.get('name'), character.get('image'),
                                    character.get('blood_type'), character.get('year_burn'),
                                    character.get('weight'), character.get('height')))


def _add_appearances_response(character):
    """Metodo para gerar a respota de character"""
    return asdict(AppearancesResponse(character.get('_id'), character.get('name'), character.get('year')))


def get_all():
    """Metodo para buscar todos os character"""
    return [_add_character_response(character) for character in _DB.find()]


def get_all_appearances(character_id: str):
    """Metodo para buscar todos os games do character"""

    filter = {
        "character_id": {"$eq": ObjectId(character_id)}
    }

    return [_add_appearances_response(character) for character in _DB_APPEARANCES.find(filter)]
