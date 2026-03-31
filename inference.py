from env.core import FuelEnv
from env.models import Action

def run(task):
    env = FuelEnv(task)
    obs = env.reset()

    
    allocations = {}

    fuel = obs.fuel_available
    requests = obs.requests

    
    if fuel >= requests["hospital"]:
        allocations["hospital"] = requests["hospital"]
        fuel -= allocations["hospital"]
    else:
        allocations["hospital"] = fuel
        fuel = 0

    if fuel > 0:
        allocations["transport"] = min(fuel, requests["transport"])
        fuel -= allocations["transport"]
    else:
        allocations["transport"] = 0

    if fuel > 0:
        allocations["public"] = min(fuel, requests["public"])
    else:
        allocations["public"] = 0

    action = Action(allocations=allocations)

    obs, reward, done, _ = env.step(action)

    return reward.score


if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        print(t, run(t))