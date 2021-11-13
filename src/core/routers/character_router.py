import json

from fastapi import APIRouter

from src.core.util import constants
from src.core.util.json_util import JSONEncoder
from src.data import read_html
from src.core.infra.queries import character_query
from src.data.command.output import response_types

router = APIRouter(tags=["Character"])


@router.get("/")
async def buscar_todos_os_personagens():
    """Retorna todos os personagens , com seus jogos"""
    return json.loads(json.dumps(character_query.get_all(), cls=JSONEncoder))


@router.get("/{character_id}/appearances")
async def buscar_todos_os_personagens(character_id: str):
    """Retorna todos os personagens , com seus jogos"""
    return json.loads(json.dumps(character_query.get_all_appearances(character_id), cls=JSONEncoder))


@router.get("/sync", response_model=response_types.ResponseBase)
async def syncroniza_os_dados():
    """Metodos que faz a importação dos dados de personagens"""
    html = read_html.read(constants.CHARACTER)
    for link in read_html.get_links(html):
        resp = read_html.read(link)
        read_html.get_character(resp)

    return {"status": "ok"}
