import uvicorn

from src.core.routers import character_router, creatures_router, games_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(character_router.router, prefix="/characters")
app.include_router(creatures_router.router, prefix="/creatures")
app.include_router(games_router.router, prefix="/games")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
