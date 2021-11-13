import json

from fastapi import APIRouter

from src.core.util import constants
from src.core.util.json_util import JSONEncoder
from src.data import read_html
from src.core.infra.queries import games_query

router = APIRouter()


@router.get("/")
async def buscar_todos_os_jogos():
    """Retorna todas os jogos"""
    return json.loads(json.dumps(games_query.get_all(), cls=JSONEncoder))


@router.get("/sync")
async def syncroniza_os_dados():
    """Metodos que faz a importação dos jogos"""
    html = read_html.read(constants.GAMES)
    for link in read_html.get_link_ul(html):
        resp = read_html.read(link)
        read_html.get_info_game(resp)

    return "ok"
