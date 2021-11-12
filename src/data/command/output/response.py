from dataclasses import dataclass


@dataclass
class GameResponse:
    id: str
    name: str
    year: str


@dataclass
class CharacterResponse:
    id: str
    name: str
    image: str
    blood_type: str
    year_burn: str
    weight: str
    height: str
    appearances: list[GameResponse]
