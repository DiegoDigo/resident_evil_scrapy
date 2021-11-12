import json

from fastapi import APIRouter

from src.core.util import constants
from src.core.util.json_util import JSONEncoder
from src.data import character, read_html

router = APIRouter()


@router.get("/")
async def buscar_todos_os_personagens():
    """Retorna todos os personagens , com seus jogos"""
    return json.loads(json.dumps(character.get_all(), cls=JSONEncoder))


@router.get("/sync")
async def syncroniza_os_dados():
    """Metodos que faz a importação dos dados de personagens"""
    html = read_html.read(constants.CHARACTER)
    for link in read_html.get_links(html):
        resp = read_html.read(link)
        read_html.get_character(resp)

    return "ok"
