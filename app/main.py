from fastapi import FastAPI
from app.api.endpoints import router as biome_router

app = FastAPI()

app.include_router(biome_router, prefix="/api", tags=["biomes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cubeium Biome API"}