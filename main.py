import uvicorn

from src.core.routers import character
from fastapi import FastAPI

app = FastAPI()
app.include_router(character.router, prefix="/characters")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
