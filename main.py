import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from src.core.routers import character_router, creatures_router, games_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(character_router.router, prefix="/characters")
app.include_router(creatures_router.router, prefix="/creatures")
app.include_router(games_router.router, prefix="/games")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
