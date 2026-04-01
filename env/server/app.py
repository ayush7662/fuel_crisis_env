from fastapi import FastAPI
from env.core import FuelEnv
from env.models import Action

app = FastAPI()
env = FuelEnv("easy")


@app.get("/")
def home():
    return {
        "message": "Fuel Crisis OpenEnv is running",
        "endpoints": {
            "reset": "/reset (POST)",
            "step": "/step (POST)",
            "state": "/state (POST)"
        },
        "docs": "/docs"
    }

@app.post("/reset")
def reset():
    return env.reset().dict()

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, info = env.step(act)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done

    }
@app.post("/state")
def state():
    return env.state()