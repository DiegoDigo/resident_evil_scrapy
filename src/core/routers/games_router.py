import json

from fastapi import APIRouter
from src.core.infra import sql

from src.core.util import constants
from src.core.util.json_util import JSONEncoder
from src.data import read_html
from src.core.infra.queries import games_query
from src.data.command.output import response_types

router = APIRouter(tags=["Games"])


@router.get("/")
async def buscar_todos_os_jogos():
    """Retorna todas os jogos"""
    return json.loads(json.dumps(games_query.get_all(), cls=JSONEncoder))


@router.get("/sync", response_model=response_types.ResponseBase)
async def syncroniza_os_dados():
    """Metodos que faz a importação dos jogos"""
    sql.drop_collection(sql.DB_GAME)
    html = read_html.read(constants.GAMES)
    for link in read_html.get_link_ul(html):
        resp = read_html.read(link)
        read_html.get_info_game(resp)

    return {"status": "ok"}


@router.get("/{game_id}/detail")
async def buscar_todos_os_jogos(game_id: str):
    """Retorna todas os jogos"""
    return json.loads(json.dumps(games_query.get_by_id(game_id), cls=JSONEncoder))
