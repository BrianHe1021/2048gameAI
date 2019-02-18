from LFAgent import LFAgent
import numpy
from random import randint, uniform
from gameboard import gameboard
import math
class QLWithLFAgent(LFAgent):
    def __init__(self, gb, lfFile):
        super().__init__(gb,lfFile)

    def learn(self):
        currentS = self.gb.board
        updateSteps = 0
        while not self.gb.islost:
            lations = self.legalAction(currentS)
            a = self.exploreOrExploitPolicy(lations)
            '''
            if updateSteps == 0:
                cs = currentS
                ca = a
                lastscore = self.gb.score
            '''
            self.gb.takeAction(a)
            nextS = self.gb.board
            '''
            if updateSteps == 5:
                updateSteps = -1
                reward = self.gb.score - lastscore
                self.update(cs, ca, reward, nextS)
            '''
            self.update(currentS, a, updateSteps, nextS)
            currentS = nextS
            updateSteps += 1
 #       self.update(cs, ca, -1, nextS)
        self.saveThetas(self.f)
        
    def update(self, cs, ca, r, ns):
        '''
        _, maxNV = self.maxQTheta(ns)
        cq, features = self.QValue(cs, ca)
        #print(features)
        if r != 0:
 #               print(r)
                r = math.log(r,2)
        for i, t in enumerate(self.thetas):
            if i >= len(features):
                break
            self.thetas[i] = t + self.alpha * (r + self.beta * maxNV - cq) * features[i]
        return
        '''
 #       print(r)
        _, maxNV = self.maxQTheta(ns)
        cq, features = self.QValue(cs, ca)
        '''
        if r > 0:
                r = (r - 300) / 100
 #       print(r)
         '''
        for v, a, i, r, c in features:
            self.thetas[a][i][r][c] = self.thetas[a][i][r][c] + self.alpha * (r + self.beta * maxNV - cq) * v
        return
        









        
        
