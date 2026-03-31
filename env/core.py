from .tasks import TASKS
from .graders import grade
from .reward import compute_reward
from .models import Observation, Action, Reward

class FuelEnv:

    def __init__(self, task_id):
        self.task_id = task_id
        self.state_data = None
        self.done = False

    def reset(self):
        data = TASKS[self.task_id]()
        self.state_data = data
        self.done = False
        return Observation(**data)
    
    def step(self, action: Action):
        grade_result = grade(self.state_data, action)
        reward = compute_reward(grade_result)

        self.done = True

        return(
            Observation(**self.state_data),
            Reward(**reward),
            self.done,
            {}
        )
    def state(self):
        return self.state_data
        
