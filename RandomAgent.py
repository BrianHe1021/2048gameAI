from agents import agent
from random import randint, uniform
class randomAgent(agent):
    def __init__(self, gb):
        super().__init__(gb)
        
    def action(self):
        return self.actions[randint(0, 3)]
