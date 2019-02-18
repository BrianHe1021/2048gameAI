from agents import agent
import numpy
from random import randint, uniform
from gameboard import gameboard
import math
from time import sleep
class LFAgent(agent):
    def __init__(self, gb, lfFile):
        super().__init__(gb)
        self.e = 0.25
        self.Q = []
        self.thetas = self.getThetas(lfFile)
        self.alpha = 0.01
        self.beta = 0.9
        self.f = lfFile
        self.corner = {(3, 0), (0, 3), (3, 3), (0, 0)}
 #       print(self.thetas)
    def action(self):
 #       sleep(0.8)
        return self.greedyPolicy()
    def learn(self):
        pass
    
    def getThetas(self, lfFile):
        '''
        f = open(lfFile, 'r')
        thetas = {}
        thetas = [float(res) for res in f.readline().split(" ")]
 #           f.readline()
        f.close()
        return thetas
        '''
        f = open(lfFile, 'r')
        thetas = {}
        for a in self.actions:
            thetas[a] = []
            for i in range(15):
                thetas[a].append([])
                '''
                if i == 0:
                    k = 4
                else:
                    k = 7
                '''
                k = 7
                for j in range(k):
                    thetas[a][i].append([float(res) for res in f.readline().split(" ")])
            f.readline()
        return thetas
    
    def greedyPolicy(self):
        a = self.maxQTheta(self.gb.board)[0]
        return a

    def maxQTheta(self, state):
        laction = self.legalAction(state)
        maxV = float('-inf')
        maxA = -1
        maxf = None
        for a in laction:
            q, f = self.QValue(state, a)
            if q > maxV:
                maxV = q
                maxA = a
                maxf = f
        if maxA == -1:
            return None, -10
 #       print(maxV)
        return maxA, maxV

    def QValue(self, state, action):
        
        """
        #features1: number of merge [0, 16]
        tempgb = gameboard(4, numpy.copy(state))
        lastNum = numpy.count_nonzero(state)
        tempgb.takeAction(action)
        mergeNum = lastNum - (numpy.count_nonzero(tempgb.board) - 1)
        mergeNum = mergeNum ** 2 / 16
        
        #features2: num of empty [0, 16]
        nempty = 16 - numpy.count_nonzero(tempgb.board)
        nempty /= 16
        #features3: reward [0, 16]
        if tempgb.score != 0:
            reward = math.log(tempgb.score, 2)
        else:
            reward = 0
        reward /= 8
#        print(r)
        #features4: MaxNum at conner 0 or 1
        m, r, c = self.getMaxNumLocation(tempgb.board)
 #       print(m,r,c)
        if (r, c) in self.corner:
            vcorner = m
        else:
            vcorner = 0
        
        #features5: monotonicity 
        mono = self.monotonicity(tempgb.board)
#        print(mono)
        '''
        if mono > 0:
            mono = math.log(mono, 2)
        mono /= 16
        '''
        
        q = mergeNum * self.thetas[0] + nempty * self.thetas[1] + reward * self.thetas[2] + vcorner + mono * self.thetas[3]
 #       print(q)
        #print(q)
        return q, (mergeNum, nempty, reward, mono)
        
        sortNum = []
 #       print(11111)
        tempgb = gameboard(4, numpy.copy(state))
        tempgb.takeAction(action)
        ss = tempgb.board
        while numpy.count_nonzero(ss) != 0:
            sNum, sR, sC = self.getMaxNumLocation(ss)
            sortNum.append((sNum, sR, sC))
            ss[sR, sC] = 0
 #       print(sortNum)
        features = []
        if len(sortNum) > 1:
            for i in range(1, len(sortNum)):
                cn, cr, cc = sortNum[i - 1]
                nn, nr, nc = sortNum[i]

                m = abs(cr - nr) + abs(cc - nc)

                v = (2 - m) * math.log(cn, 2)
                features.append(v)

        q = tempgb.score + mergeNum
        for f in features:
            q += f
 #       print(features)
        return q, features
        """
        ss = numpy.copy(state)
        sortNum = []
        while numpy.count_nonzero(ss) != 0:
            sNum, sR, sC = self.getMaxNumLocation(ss)
            sortNum.append((sNum, sR, sC))
            ss[sR, sC] = 0
 #       print(sortNum)
        
 #       tempgb = gameboard(4, numpy.copy(state))
#        tempgb.takeAction(action)

        '''
        features = []
        maxN, maxR, maxC = sortNum[0]
        q = math.log(maxN, 2) * self.thetas[action][0][maxR][maxC]
        features.append((math.log(maxN, 2), action, 0, maxR, maxC))
        '''
        features = []
        maxN, maxR, maxC = sortNum[0]
        q = 0
        lastR = maxR
        lastC = maxC
        lastN = maxN
        
        for i, (n, r, c) in enumerate(sortNum[1:]):
            v = 1 / (math.log(lastN, 2) - math.log(n, 2) + 1)
 #           print(v)
            q += v * self.thetas[action][i][r - lastR + 3][c - lastC + 3]
            features.append((v, action, i, r - lastR + 3, c - lastC + 3))
            lastR = r
            lastC = c
            lastN = n
            

        return q, features
    def getNumSum(self, state):
        maxNum, _, _ = self.getMaxNumLocation(state)
        v = 0
        while maxNum != 1:
            if numpy.any(state == maxNum):
                v += maxNum
            maxNum /= 2
        return v
    def monotonicity(self, state, v = 0):

        maxNum, maxR, maxC = self.getMaxNumLocation(state)
        v = 0
        sortNum = []
        ss = numpy.copy(state)

        if (maxR, maxC) not in self.corner:
            return 0
        '''
        while numpy.count_nonzero(ss) != 0:
            sNum, sR, sC = self.getMaxNumLocation(ss)
            sortNum.append(sNum)
            ss[sR, sC] = 0
        '''
        if (maxR, maxC) == (0, 3):
            stateC = numpy.rot90(state, 1)
        elif (maxR, maxC) == (3, 3):
            stateC = numpy.rot90(state, 2)
        elif (maxR, maxC) == (3, 0):
            stateC = numpy.rot90(state, 3)
        else:
            stateC = numpy.copy(state)
            
        for i in range(4):
            for k in range(1,4):
 #               if state[i,k] == 0:
#                    break
 #               if state[i,k] < state[i, k - 1]:
 #                   v += state[i,k]
                v += state[i, k - 1] + state[i,k]
#                else:
#                    break

        for j in range(4):
            for k in range(1,4):
  #              if state[k, j] == 0:
#                    break
#                if state[k, j] < state[ k - 1, j]:
 #                   v += state[k,j]
                    v += state[k - 1, j] + state[k, j]
#                else:
#                    break
        '''
        for x in sortNum:
 #           print(i,j)
            if state[i,j] == x:
                v += x
            j += adj
            if j == 4 or j == -1:
                adj *= -1
                j += adj
                i += 1
        '''
                
 #       print(stateC)
#        print(v)
        return v
                        
    def exploreOrExploitPolicy(self, lactions):
        p = uniform(0, 1)
        if p < self.e:
            return lactions[randint(0, len(lactions) - 1)]
        else:
            return self.greedyPolicy()
    
    def getMaxNumLocation(self, state):
        maxNum = numpy.amax(state)
        mlocation = {}
        for i in range(4):
            for j in range(4):
                if state[i,j] == maxNum:
                    mlocation[i, j] = 0
        for (i,j) in [(0,0), (0,3), (3,0), (3,3)]:
            if (i,j) in mlocation:
                return maxNum, i, j
        maxLoaction = numpy.argmax(state)
        maxR, maxC = maxLoaction // 4, maxLoaction % 4
        return maxNum, maxR, maxC
    
    def legalAction(self, state):
        la = ['u', 'd', 'l', 'r']
        for a in self.actions:
            tempgb = gameboard(4, numpy.copy(state))
            changed = tempgb.takeAction(a)
            if not changed:
                la.remove(a)
        return la

    def saveThetas(self, filename):
        '''
        f = open(filename, 'w')
        if max(self.thetas) > 100:
            adject = 100
        else:
            adject = 1
        for i, n in enumerate(self.thetas):
            f.write(str(n / adject))
            if i != len(self.thetas) - 1:
                f.write(" ")
            else:
                f.write("\n")
        f.write("\n")
        f.close()
        '''
        f = open(filename, 'w')

        for a in self.actions:
            for i in range(15):
                '''
                if i == 0:
                    n = 4
                else:
                    n = 7
                '''
                n = 7
                for j in range(n):
                    for k in range(n):
                        f.write(str(self.thetas[a][i][j][k]))
                        if k == 6:
                            f.write("\n")
                        else:
                            f.write(" ")
            f.write("\n")
        f.close()
