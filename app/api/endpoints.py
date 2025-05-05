from fastapi import APIRouter, HTTPException
from app.models.biome import BiomeRequest, BiomeResponse
from app.services.biome_service import get_biome_data

router = APIRouter()

@router.post("/api/biomes", response_model=BiomeResponse)
async def biome_endpoint(biome_request: BiomeRequest):
    biome_data = await get_biome_data(biome_request.seed)
    if biome_data is None:
        raise HTTPException(status_code=404, detail="Biome data not found")
    return biome_data