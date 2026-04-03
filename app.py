import uvicorn
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
            "state": "/state (POST)",
        },
        "docs": "/docs",
    }


@app.post("/reset")
def reset():
    return env.reset().dict()


@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, _info = env.step(act)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done,
    }


@app.post("/state")
def state():
    return env.state()


def main():
    uvicorn.run("app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
