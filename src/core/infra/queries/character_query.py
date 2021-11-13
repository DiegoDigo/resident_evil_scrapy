from dataclasses import asdict

from src.core.infra import sql
from src.data.command.output.response import CharacterResponse, AppearancesResponse

_DB = sql.DB_CHARACTER


def _get_games_response(games) -> list[AppearancesResponse]:
    """Metodo para gerar a respota de games"""
    return [asdict(AppearancesResponse(game.get('_id'), game.get('name'), game.get('year'))) for game in games]


def _add_character_response(character):
    """Metodo para gerar a respota de character"""
    return asdict(CharacterResponse(character.get('_id'), character.get('name'), character.get('image'),
                                    character.get('blood_type'), character.get('year_burn'),
                                    character.get('weight'), character.get('height'),
                                    _get_games_response(character.get('games'))))


def get_all():
    """Metodo para buscar todos os character com seus gamoes"""
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

    return [_add_character_response(character) for character in _DB.aggregate(pipeline)]
