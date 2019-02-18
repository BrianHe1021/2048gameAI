import agents
from MCAgent import MCAgent
from RandomAgent import randomAgent
from UCTAgent import UCTAgent
from QLWithLFAgent import QLWithLFAgent
from SARSAWithLFAgent import SARSAWithLFAgent
from MCWithLF import MCWithLFAgent
from TDAgent import QLAgent, SARSAAgent
from gameboard import gameboard
import time
import os
from threading import Thread, Lock, Semaphore
from time import sleep
import shutil
agentType = {"MCAgent": MCAgent}
def main():
    
    gb = gameboard(4, isPrint = True)
    agent = UCTAgent(gb, 15, 500)
    agent.play()
    print("game over. The score is " + str(gb.score))
                  

    # collecting data from here
    '''
    tscore = 0
    
    for i in range(500):
        gb = gameboard(4)
        agent = randomAgent(gb)
        agent.play()
        tscore += gb.score
    print(tscore/500)
    '''
    
    '''
    gb = gameboard(4, isPrint = True)
    agent = randomAgent(gb)
    while not gb.islost:
        gb.takeAction(agent.action())
    '''
    
    
    #MCAgent
#    os.system('say "start"')
 #   ss = 500
#    s = 15
    """
    stepLimited = [50]
    simulationN = [500]
    
    for sn in simulationN:
        for sl in stepLimited:
            f = open("results/MCResult.txt", 'a')
            f.write("************** sn:" + str(sn) + ", sl:" + str(sl) + "*************\n")
            f.close()
            tscore = 0
            print("now sn:" + str(sn) + ", sl:" + str(sl))
            for i in range(1, 20):
                f = open("results/MCResult.txt", 'a')
                gb = gameboard(4, isPrint = False)
                agent = MCAgent(gb, sl, sn)
                agent.play()
                
                tscore += gb.score
                f.write(str(i) + ":\n")
                f.write("average score: " + str(tscore / i) + "\n")
                f.write("score: " + str(gb.score) + "\n")
                f.close()
    
    """
    """
    for sn in simulationN:
        for sl in stepLimited:
            f = open("results/UCTResult.txt", 'a')
            f.write("************** sn:" + str(sn) + ", sl:" + str(sl) + "*************\n")
            f.close()
            tscore = 0
            print("now sn:" + str(sn) + ", sl:" + str(sl))
            for i in range(1, 20):
                f = open("results/UCTResult.txt", 'a')
                gb = gameboard(4, isPrint = False)
                agent = UCTAgent(gb, sl, sn)
                agent.play()
                
                tscore += gb.score
                f.write(str(i) + ":\n")
                f.write("average score: " + str(tscore / i) + "\n")
                f.write("score: " + str(gb.score) + "\n")
                f.close()
                  
    """
    """
    learningFile = "QLtest.txt"
    
    tscore = 0
    for i in range(1, 100000):
        gb = gameboard(4, isPrint = False)
        agent = QLWithLFAgent(gb, learningFile)
        '''
        agent.learn()
        if i in {100, 300, 500,1000,3000,6000,10000, 15000, 20000, 30000, 50000, 100000}:
            print(i)
        print(i)
        #'''
        
        #'''
        agent.play()
        print(gb.score)
        tscore += gb.score
        print("average: " + str(tscore / i))
        #'''
    """
    
     #   os.system('say "new outcome"')
    
    """
    learningFile = "MCtest.txt"
    
    learningRF = "MCLearning"
    tscore = 0
    for i in range(1, 100000000):
        gb = gameboard(4, isPrint = False)
        agent = MCWithLFAgent(gb, learningFile)
        '''
        agent.learn()
        print(i)
        if i % 10 == 0:
            copyFiles("MCtest.txt", "MCLF/MCLearning" + str(i) + ".txt")
        #'''
        #'''
        agent.play()
        print(gb.score)
        tscore += gb.score
        print("average: " + str(tscore / i))
        #'''
    """
    
    """
    learningRF = "MCLF/MCLearning"
    resultFile = "results/MC_LF.txt"
    for li in range(0, 2000, 10):
        tscore = 0
        lf = learningRF + str(li) + ".txt"
        rf = open(resultFile, "a")
        rf.write(str(li) + ":\n")
        for i in range(1, 30):
            gb = gameboard(4, isPrint = False)
            agent = MCWithLFAgent(gb, lf)
            agent.play()

            tscore += gb.score
            
        rf.write("average score: " + str(tscore / i) + "\n")
        rf.close()
    """
    """
    learningFile = "SARSAtest.txt"
    
    tscore = 0
    for i in range(1, 500):
        gb = gameboard(4, isPrint = False)
        agent = QLWithLFAgent(gb, learningFile)
        '''
        agent.learn()
        if i in {100, 500,1000,3000,6000,10000, 15000, 20000, 30000, 50000, 100000}:
            print(i)
        #'''
        '''
        agent.play()
        print(gb.score)
        tscore += gb.score
        print("average: " + str(tscore / i))
        #'''
    """
    """
    ss = 500
    s = 15
#    f = open("res_steps" + "(" + str(s) + ")" + ".txt" , "a")
#    f.write("********res of " + str(s) + "***********\n")
#    f.close()
    tscore = 0
    for i in range(1, 15):
 #       f = open("res_steps" + "(" + str(s) + ")" + ".txt", "a")
        gb = gameboard(4, isPrint = True)
        agent = UCTAgentWithS(gb, s, ss)
        agent.play()
    

        tscore += gb.score
        print(str(tscore) + "(" + str(gb.score) +")")
 #       f.write(str(i) + ": " + str(tscore / i) + " (" + str(gb.score) + ")\n")
        
        os.system('say "new outcome"')
    """
    """
    for sn in simulationN:
        for sl in stepLimited:
            f = open("results/QLResult.txt", 'a')
            f.write("************** sn:" + str(sn) + ", sl:" + str(sl) + "*************\n")
            f.close()
            tscore = 0
            print("now sn:" + str(sn) + ", sl:" + str(sl))
            for i in range(1, 20):
                f = open("results/QLResult.txt", 'a')
                gb = gameboard(4, isPrint = False)
                agent = QLAgent(gb, sl, sn)
                agent.play()
                
                tscore += gb.score
                f.write(str(i) + ":\n")
                f.write("average score: " + str(tscore / i) + "\n")
                f.write("score: " + str(gb.score) + "\n")
                f.close()
                    
    
    """
    """
    for sn in simulationN:
        for sl in stepLimited:
            f = open("results/SARSAResult.txt", 'a')
            f.write("************** sn:" + str(sn) + ", sl:" + str(sl) + "*************\n")
            f.close()
            tscore = 0
            print("now sn:" + str(sn) + ", sl:" + str(sl))
            for i in range(1, 20):
                f = open("results/SARSAResult.txt", 'a')
                gb = gameboard(4, isPrint = False)
                agent = SARSAAgent(gb, sl, sn)
                agent.play()
                
                tscore += gb.score
                f.write(str(i) + ":\n")
                f.write("average score: " + str(tscore / i) + "\n")
                f.write("score: " + str(gb.score) + "\n")
                f.close()
     """                 

def copyFiles(sourceDir,  targetDir): 
    shutil.copy(sourceDir,  targetDir)
main()

