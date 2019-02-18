import matplotlib.pyplot as plt
import pylab as pl
allData = {}
def getData(filename):
    f = open(filename,"r")
 #   print(filename)
 #   allData[filename] = []
    data = {}
    for sn, sl in [(100, 10), (100, 15),(100, 20),(300, 10),(300, 15),(300, 20),(500, 10),(500, 15),(500, 20),(100, 50),(100, 100),(300, 50),(300, 100),(500, 50), (500, 100)]:
 #       if filename in {"results/SARSAResult.txt","results/MCResult.txt"} and (sn,sl) in {(500, 50), (500, 100)}:
#            continue
        f.readline()
 #       print(sn,sl)
        data[sn, sl] = []
 #       print(sn,sl)
        for _ in range(19):
            f.readline()
            
#            s = f.readline().split(" ")
 #           print(s)
            s = float(f.readline().split(" ")[2])
            f.readline()
            data[sn, sl].append(s)
 #   print(data)
    allData[filename] = data

def getFLData(filename):
    f = open(filename,"r")
    data = []
    for _ in range(200):
        f.readline()
        s = float(f.readline().split(" ")[2])
        data.append(s)
    allData[filename] = data
getData("results/UCTResult.txt")
getData("results/QLResult.txt")
getData("results/SARSAResult.txt")
getData("results/MCResult.txt")
getFLData("results/MC_LF.txt")

Filenames = {"results/UCTResult.txt" : "UCT", "results/QLResult.txt" : "QL","results/SARSAResult.txt" : "SARSA","results/MCResult.txt" : "MC"}
def draw():

    def sameSLOfAllAgents(sl):
        datas = {}
     #   sl = 20
        filename = "results/AA " + str(sl) + " steps limited"
        snData = [100, 300, 500]
        for fn in ["results/UCTResult.txt", "results/QLResult.txt", "results/SARSAResult.txt", "results/MCResult.txt"]:
            datas[fn] = []
            for sn in snData:
     #           print(fn, sn, sl )
                datas[fn].append(allData[fn][sn,sl][18])
                
        
        Fig = plt.figure(figsize=(8,4))
        Ax = Fig.add_subplot(111)
        pl.title("Performance of all agents with " + str(sl) + " steps limitaion")
        pl.xlabel("Number of Trials")
        pl.ylabel("Average Score")
        pl.xticks([100, 300, 500])
        Ax.plot( snData, datas["results/UCTResult.txt"], snData, datas["results/QLResult.txt"],snData, datas["results/SARSAResult.txt"], snData, datas["results/MCResult.txt"])
        Ax.legend(["UCT agent", "QL agent", "SARSA agent", "MC agent"])
        Fig.savefig(filename + ".png")

    def sameSNOfAllAgents(sn):
        datas = {}
 #       sn = 300
        filename = "results/AA " + str(sn) + " learning trials"
        slData = [10, 15, 20, 50, 100]
        for fn in ["results/UCTResult.txt", "results/QLResult.txt", "results/SARSAResult.txt", "results/MCResult.txt"]:
            datas[fn] = []
            for sl in slData:
     #           print(fn, sn, sl )
                datas[fn].append(allData[fn][sn,sl][18])
                
        
        Fig = plt.figure(figsize=(8,4))
        Ax = Fig.add_subplot(111)
        pl.title("Performance of all agents with " + str(sn) + " learning trials")
        pl.xlabel("Limited Step")
        pl.ylabel("Average Score")
        pl.xticks([10, 20, 30, 40, 50, 60 ,70, 80, 90, 100])
        Ax.plot( slData, datas["results/UCTResult.txt"], slData, datas["results/QLResult.txt"],slData, datas["results/SARSAResult.txt"], slData, datas["results/MCResult.txt"])
        Ax.legend(["UCT agent", "QL agent", "SARSA agent", "MC agent"])
        Fig.savefig(filename + ".png")

    

    def compareSL(fn):
        datas = {}
        snData = [100, 300, 500]
        slData = [10, 15, 20, 50, 100]
        filename = "results/" + Filenames[fn] + " (sl) "
        for sn in snData:
            datas[sn] = []
            for sl in slData:
                datas[sn].append(allData[fn][sn,sl][18])
        Fig = plt.figure(figsize=(8,4))
        Ax = Fig.add_subplot(111)
        pl.title("Performance of " + Filenames[fn] + " with increasing limited step")
        pl.xlabel("Limited Step")
        pl.ylabel("Average Score")
        pl.xticks([10, 20, 30, 40, 50, 60 ,70, 80, 90, 100])
        Ax.plot( slData, datas[100], slData, datas[300],slData, datas[500])
        Ax.legend(["100 Trials", "300 Trials","500 Trials"])
        Fig.savefig(filename + ".png")
        
    def compareSN(fn):
        datas = {}
        snData = [100, 300, 500]
        slData = [10, 15, 20, 50, 100]
        filename = "results/" + Filenames[fn] + " (sn) "
        for sl in slData:
            datas[sl] = []
            for sn in snData:
                datas[sl].append(allData[fn][sn,sl][18])
        Fig = plt.figure(figsize=(8,4))
        Ax = Fig.add_subplot(111)
        pl.title("Performance of " + Filenames[fn] + " with increasing learning trials")
        pl.xlabel("learning trials")
        pl.ylabel("Average Score")
        pl.xticks([100, 300, 500])
        Ax.plot( snData, datas[10],snData, datas[15],snData, datas[20],snData, datas[50],snData, datas[100] )
        Ax.legend(["10 limited steps","15 limited steps","20 limited steps","50 limited steps","100 limited steps",])
        Fig.savefig(filename + ".png")
        
    datax = []
    for i in range(0, 200000, 1000):
        datax.append(i)
    fn = "results/MC_LF.txt"
    datay = allData[fn]
    Fig = plt.figure(figsize=(8,4))
    Ax = Fig.add_subplot(111)
    pl.title("Monte Carol Agent With Linear Function")
    pl.xlabel("Learning Episode")
    pl.ylabel("Average Score")
    Ax.plot( datax, datay)
#    Ax.legend(["100 Trials", "300 Trials","500 Trials"])
    Fig.savefig("Monte Carol Agent With Linear Function" + ".pdf")
    '''
    datas = {}
    fn = "results/QLResult.txt"
    snData = [100, 300, 500]
    slData = [10, 15, 20, 50, 100]
    for sn in snData:
        datas[sn] = []
        for sl in slData:
            datas[sn].append(allData[fn][sn,sl][18])
    Fig = plt.figure(figsize=(8,4))
    Ax = Fig.add_subplot(111)
    pl.title("Performance of Q-Learning with increasing limited step")
    pl.xlabel("Limited Step")
    pl.ylabel("Average Score")
    pl.xticks([10, 20, 30, 40, 50, 60 ,70, 80, 90, 100])
    Ax.plot( slData, datas[100], slData, datas[300],slData, datas[500])
    Ax.legend(["100 Trials", "300 Trials","500 Trials"])
    Fig.savefig("test4" + ".pdf")
    '''

        
    '''
    datas = {}
    fn = "results/UCTResult.txt"
    snData = [100, 300, 500]
    slData = [10, 15, 20, 50, 100]
    for sn in snData:
        datas[sn] = []
        for sl in slData:
            datas[sn].append(allData[fn][sn,sl][18])
    Fig = plt.figure(figsize=(8,4))
    Ax = Fig.add_subplot(111)
    pl.title("Performace of UCT")
    pl.xlabel("Limited Step")
    pl.ylabel("Average Score")
    pl.xticks([10, 20, 30, 40, 50, 60 ,70, 80, 90, 100])
    Ax.plot( slData, datas[100], slData, datas[300],slData, datas[500])
    Ax.legend(["100 Trials", "300 Trials","500 Trials"])
    Fig.savefig("test5" + ".pdf")

    datas = {}
    fn = "results/QLResult.txt"
    snData = [100, 300, 500]
    slData = [10, 15, 20, 50, 100]
    for sn in snData:
        datas[sn] = []
        for sl in slData:
            datas[sn].append(allData[fn][sn,sl][18])
    Fig = plt.figure(figsize=(8,4))
    Ax = Fig.add_subplot(111)
    pl.title("Performace of Q-Learning")
    pl.xlabel("Limited Step")
    pl.ylabel("Average Score")
    pl.xticks([10, 20, 30, 40, 50, 60 ,70, 80, 90, 100])
    Ax.plot( slData, datas[100], slData, datas[300],slData, datas[500])
    Ax.legend(["100 Trials", "300 Trials","500 Trials"])
    Fig.savefig("test6" + ".pdf")
    '''
    sameSNOfAllAgents(100)
    sameSNOfAllAgents(300)
    sameSNOfAllAgents(500)
    sameSLOfAllAgents(10)
    sameSLOfAllAgents(15)
    sameSLOfAllAgents(20)
    sameSLOfAllAgents(50)
    sameSLOfAllAgents(100)
    compareSL("results/UCTResult.txt")
    compareSL("results/QLResult.txt")
    compareSL("results/SARSAResult.txt")
    compareSL("results/MCResult.txt")
    compareSN("results/UCTResult.txt")
    compareSN("results/QLResult.txt")
    compareSN("results/SARSAResult.txt")
    compareSN("results/MCResult.txt")
#print(allData)
draw()
