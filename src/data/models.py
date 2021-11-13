from typing import Optional
from dataclasses import dataclass, asdict

from src.core.infra import sql


@dataclass
class Game:
    name: str
    year: str
    character_id: Optional[str]

    def save(self):
        doc = sql.DB_GAME
        return doc.insert_one(asdict(self)).inserted_id


@dataclass
class Character:
    name: str
    year_burn: str
    blood_type: str
    height: str
    weight: str
    image: str

    def save(self):
        doc = sql.DB_CHARACTER
        return doc.insert_one(asdict(self)).inserted_id


@dataclass
class Creature:
    name: str
    image: str

    def save(self):
        doc = sql.DB_CREATURE
        return doc.insert_one(asdict(self)).inserted_id
