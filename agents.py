class agent():
    def __init__(self, gb):#, mutex = None):
        self.gb = gb
        self.actions = ['u', 'd', 'l', 'r']
        self.score = 0
        self.rewardOfActions = []
 #       self.mutex = mutex
    def action(self):
        pass
    def play(self):
        while not self.gb.islost:
            self.gb.takeAction(self.action())
