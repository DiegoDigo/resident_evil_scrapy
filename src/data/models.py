from typing import Optional
from dataclasses import dataclass, asdict

from src.core import sql


@dataclass
class Game:
    name: str
    year: str
    character_id: Optional[str]

    def save(self):
        game_table = sql.DB_GAME
        return game_table.insert_one(asdict(self)).inserted_id


@dataclass
class Character:
    name: str
    year_burn: str
    blood_type: str
    height: str
    weight: str
    image: str

    def save(self):
        character_table = sql.DB_CHARACTER
        return character_table.insert_one(asdict(self)).inserted_id
