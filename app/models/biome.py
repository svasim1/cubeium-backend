from pydantic import BaseModel
from typing import List, Optional

class Biome(BaseModel):
    id: int
    name: str
    temperature: float
    precipitation: float
    vegetation: List[str]

class BiomeRequest(BaseModel):
    seed: str

class BiomeResponse(BaseModel):
    biome: Biome
    message: Optional[str] = None