from pydantic import BaseModel

from src.data.command.output import response_models


class ResponseListGame(BaseModel, response_models.GameResponse):
    pass


class ResponseGame(BaseModel, response_models.GameResponse):
    pass


class ResponseBase(BaseModel):
    status: str


class ResponseCharacter(BaseModel, response_models.CharacterResponse):
    pass
