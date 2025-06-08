from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from src.simulation import create_agents, World

app = FastAPI(title="Ecosystem Simulator")

class SimulationRequest(BaseModel):
    num_agents: int = 10
    steps: int = 3

class SimulationResponse(BaseModel):
    events: List[List[str]]


def run_simulation(num_agents: int, steps: int) -> List[List[str]]:
    agents = create_agents(num_agents)
    world = World(agents)
    all_events: List[List[str]] = []
    for _ in range(steps):
        events = world.step()
        all_events.append(events)
    return all_events

@app.get("/")
async def root():
    return {"message": "Ecosystem Simulator is running"}

@app.post("/simulate", response_model=SimulationResponse)
async def simulate(req: SimulationRequest):
    events = run_simulation(req.num_agents, req.steps)
    return {"events": events}
