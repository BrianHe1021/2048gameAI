from LFAgent import LFAgent
import numpy
from random import randint, uniform
from gameboard import gameboard
import math
class MCWithLFAgent(LFAgent):
    def __init__(self, gb, lfFile):
        super().__init__(gb,lfFile)
 #       self.beta = 0.9
    def learn(self):
        
        self.updateSequence = []

        while not self.gb.islost:
            cs = numpy.copy(self.gb.board)
            lactions = self.legalAction(cs)
            ca = self.exploreOrExploitPolicy(lactions)
            lastscore = self.gb.score
            self.gb.takeAction(ca)
            r = self.gb.score - lastscore
            if self.gb.islost:
                r -= self.gb.score * 0.1
            self.updateSequence.append((numpy.copy(cs), ca, r))
#        print(self.updateSequence)
 #       self.updateSequence[len(self.updateSequence) - 1][2] 
        self.update()
        self.saveThetas(self.f)
        
    def update(self, score = 0):
        """
        for i, (cs, ca, r) in enumerate(self.updateSequence[::-1]):
 #           print(cs,ca,r)
            cq, features = self.QValue(cs, ca)
            cv = self.score * (self.beta ** i)
            if len(features) == 0:
                continue
            
            for v, a, i, r, c in features:
                self.thetas[ca][i][r][c] = self.thetas[ca][i][r][c] + self.alpha * (cv - cq) * v
        """
        
        for i, (cs, ca, r) in enumerate(self.updateSequence):
 #           print(cs,ca,r)
        
            cq, features = self.QValue(cs, ca)
            cv = 0
            for j, (_, _, r) in enumerate(self.updateSequence[i:]):
                cv += r * (self.beta ** j)
 #           print(cv,cq)
           
            for v, a, ii, r, c in features:
                self.thetas[ca][ii][r][c] = self.thetas[ca][ii][r][c] + self.alpha * (cv - cq) * v
        
        

        
        '''
        for i, (cs, ca, r) in enumerate(self.updateSequence):
            cq, features = self.QValue(cs, ca)
            cv = r
       
            for v, a, i, r, c in features:
                self.thetas[ca][i][r][c] = self.thetas[ca][i][r][c] + self.alpha * (cv - cq) * v
        '''





        
        
