import uvicorn

from src.core.routers import character, creatures
from fastapi import FastAPI

app = FastAPI()
app.include_router(character.router, prefix="/characters")
app.include_router(creatures.router, prefix="/creatures")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
