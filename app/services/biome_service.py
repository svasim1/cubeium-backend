from typing import List
from fastapi import HTTPException
from app.models.biome import Biome, BiomeCreate

# Mock database for demonstration purposes
mock_biome_data = {}

def get_biome(seed: str) -> Biome:
    if seed in mock_biome_data:
        return mock_biome_data[seed]
    raise HTTPException(status_code=404, detail="Biome not found")

def create_biome(biome_create: BiomeCreate) -> Biome:
    if biome_create.seed in mock_biome_data:
        raise HTTPException(status_code=400, detail="Biome already exists")
    
    biome = Biome(**biome_create.dict())
    mock_biome_data[biome_create.seed] = biome
    return biome

def list_biomes() -> List[Biome]:
    return list(mock_biome_data.values())