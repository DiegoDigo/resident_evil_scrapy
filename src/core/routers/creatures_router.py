import json

from fastapi import APIRouter
from src.core.infra import sql

from src.core.util import constants
from src.core.util.json_util import JSONEncoder
from src.data import read_html
from src.core.infra.queries import creatures_query

router = APIRouter(tags=["Creatures"])


@router.get("/")
async def buscar_todos_as_criaturas():
    """Retorna todas as criaturas do jogos"""
    return json.loads(json.dumps(creatures_query.get_all(), cls=JSONEncoder))


@router.get("/sync")
async def syncroniza_os_dados():
    """Metodos que faz a importação das criaturas"""
    sql.drop_colection(sql.DB_CREATURE)
    html = read_html.read(constants.CREATURES)
    for link in read_html.get_links(html):
        resp = read_html.read(link)
        read_html.get_creature(resp)

    return "ok"
