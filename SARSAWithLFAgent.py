from LFAgent import LFAgent
import numpy
import math
class SARSAWithLFAgent(LFAgent):
    def __init__(self, gb, lfFile):
        super().__init__(gb,lfFile)

    def learn(self):
        cs = self.gb.board
        lations = self.legalAction(cs)
        ca = self.exploreOrExploitPolicy(lations)
        while not self.gb.islost:
            lastscore = self.gb.score
            self.gb.takeAction(ca)
            if self.gb.islost:
                break
            ns = self.gb.board
            lations = self.legalAction(ns)
            na = self.exploreOrExploitPolicy(lations)
 #           print(na)
    
            reward = self.gb.score - lastscore
            self.update(cs, ca, reward, ns, na)
            cs = ns
            ca = na
        self.saveThetas(self.f)
        
    def update(self, cs, ca, r, ns, na):
        cq, features = self.QValue(cs, ca)
        nq, _ = self.QValue(ns, na)
        for i, t in enumerate(self.thetas):
            self.thetas[i] = t + self.alpha * (r + self.beta * nq - cq) * features[i]
        return
