from pydantic import BaseModel
from typing import Dict

class Observation(BaseModel):
    fuel_available: int
    requests: Dict[str, int]
    urgency: str

class Action (BaseModel):
    allocations: Dict[str, int]

class Reward(BaseModel):
    score: float
    breakdown: Dict[str, float]