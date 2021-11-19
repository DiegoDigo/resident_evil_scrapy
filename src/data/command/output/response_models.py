from dataclasses import dataclass


@dataclass
class AppearancesResponse:
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


@dataclass
class CreatureResponse:
    id: str
    name: str
    image: str
    description: str
    strategies: str


@dataclass
class GameResponse:
    id: str
    name: str
    image: str
    synopsis: str
    release: list[str]
