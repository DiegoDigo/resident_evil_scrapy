from dataclasses import asdict

from src.core.infra import sql
from src.data.command.output.response_models import CreatureResponse

_DB = sql.DB_CREATURE


def _add_creature_response(character):
    """Metodo para gerar a respota de character"""
    return asdict(CreatureResponse(character.get('_id'), character.get('name'), character.get('image')))


def get_all():
    """Metodo para buscar todos os character com seus gamoes"""
    return [_add_creature_response(character) for character in _DB.find()]
