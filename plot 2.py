from matplotlib import pyplot as plt
import io
'''
def loadfile(filename):
	file = io.open(filename,'r')
	content = file.readlines()
	point = []
	#for i in range(len(content)):
	for j in content:
		index = 1
		if j[0:1]=="s":
			m=j.split()
			point.append(int(m[1]))
	part1_100_10 = []
	part1_100_15 = []
	part1_100_20 = []
	part1_300_10 = []
	part1_300_15 = []
	part1_300_20 = []
	part1_500_10 = []
	part1_500_15 = []
	part1_500_20 = []
	part1_100_50 = []
	part1_100_100 = []
	part1_300_50 = []
	part1_300_100 = []
	part1_500_50 = []
	part1_500_100 = []
	for x in range(19):
		part1_100_10.append(point[x])
	for x in range(19, 38):
		part1_100_15.append(point[x])
	for x in range(38, 38+19):
		part1_100_20.append(point[x])
	for x in range(38+19, 38+19*2):
		part1_300_10.append(point[x])
	for x in range(38+19*2, 38+19*3):
		part1_300_15.append(point[x])
	for x in range(38+19*3, 38+19*4):
		part1_300_20.append(point[x])
	for x in range(38+19*4, 38+19*5):
		part1_500_10.append(point[x])
	for x in range(38+19*5, 38+19*6):
		part1_500_15.append(point[x])
	for x in range(38+19*6, 38+19*7):
		part1_500_20.append(point[x])
	for x in range(38+19*7, 38+19*8):
		part1_100_50.append(point[x])
	for x in range(38+19*8, 38+19*9):
		part1_100_100.append(point[x])
	for x in range(38+19*9, 38+19*10):
		part1_300_50.append(point[x])
	for x in range(38+19*10, 38+19*11):
		part1_300_100.append(point[x])
	for x in range(38+19*11, 38+19*12):
		part1_500_50.append(point[x])
	for x in range(38+19*12, 38+19*13):
		part1_500_100.append(point[x])
	#point1=[]
	#point1.append([])
	xaxis=[]
	for x in range(1, 20):
		xaxis.append(int(x))
	plt.scatter(xaxis, part1_300_10, c='r', marker='o')
	plt.scatter(xaxis, part1_300_50, c='g', marker='x')
	plt.scatter(xaxis, part1_300_100, c='b', marker='*')
	plt.xlim([0,20])
	plt.xlabel('Game number')
	plt.ylabel('Score')
	plt.xticks(range(len(xaxis)+2))
	plt.title('Performance of UCT with learning trial = 300')
	plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	plt.savefig("Performance of UCT(POINT).jpg")
	#plt.scatter(xaxis, part1_300_10, c='r', marker='o')
	#plt.scatter(xaxis, part1_300_50, c='g', marker='x')
	#plt.scatter(xaxis, part1_300_100, c='b', marker='*')
	#plt.xlim([0,20])
	#plt.xlabel('game number')
	#plt.ylabel('Score')
	#plt.xticks(range(len(xaxis)+2))
	#plt.title('Performance of UCT with learning trial = 300')
	#plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	#plt.savefig("Performance of UCT(POINT).jpg")
	#point = []
	#for i in range()
	#	line1 = content[3+ 3*i].split()
	#	point.append(line1[1])

#loadfile("./results/UCTResult.txt")

from matplotlib import pyplot as plt
import io

def loadfile2(filename):
	file = io.open(filename,'r')
	content = file.readlines()
	point = []
	#for i in range(len(content)):
	for j in content:
		index = 1
		if j[0:1]=="s":
			m=j.split()
			point.append(int(m[1]))
	part1_100_10 = []
	part1_100_15 = []
	part1_100_20 = []
	part1_300_10 = []
	part1_300_15 = []
	part1_300_20 = []
	part1_500_10 = []
	part1_500_15 = []
	part1_500_20 = []
	part1_100_50 = []
	part1_100_100 = []
	part1_300_50 = []
	part1_300_100 = []
	part1_500_50 = []
	part1_500_100 = []
	for x in range(19):
		part1_100_10.append(point[x])
	for x in range(19, 38):
		part1_100_15.append(point[x])
	for x in range(38, 38+19):
		part1_100_20.append(point[x])
	for x in range(38+19, 38+19*2):
		part1_300_10.append(point[x])
	for x in range(38+19*2, 38+19*3):
		part1_300_15.append(point[x])
	for x in range(38+19*3, 38+19*4):
		part1_300_20.append(point[x])
	for x in range(38+19*4, 38+19*5):
		part1_500_10.append(point[x])
	for x in range(38+19*5, 38+19*6):
		part1_500_15.append(point[x])
	for x in range(38+19*6, 38+19*7):
		part1_500_20.append(point[x])
	for x in range(38+19*7, 38+19*8):
		part1_100_50.append(point[x])
	for x in range(38+19*8, 38+19*9):
		part1_100_100.append(point[x])
	for x in range(38+19*9, 38+19*10):
		part1_300_50.append(point[x])
	for x in range(38+19*10, 38+19*11):
		part1_300_100.append(point[x])
	for x in range(38+19*11, 38+19*12):
		part1_500_50.append(point[x])
	for x in range(38+19*12, 38+19*13):
		part1_500_100.append(point[x])
	#point1=[]
	#point1.append([])
	xaxis=[]
	for x in range(1, 20):
		xaxis.append(int(x))
	plt.scatter(xaxis, part1_300_10, c='r', marker='o')
	plt.scatter(xaxis, part1_300_50, c='g', marker='x')
	plt.scatter(xaxis, part1_300_100, c='b', marker='*')
	plt.xlim([0,20])
	plt.xlabel('Game number')
	plt.ylabel('Score')
	plt.xticks(range(len(xaxis)+2))
	plt.title('Performance of q_learning with learning trial = 300')
	plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	plt.savefig("Performance of q_learning(POINT).jpg")
	#point = []
	#for i in range()
	#	line1 = content[3+ 3*i].split()
	#	point.append(line1[1])

loadfile2("./results/QLResult.txt")

def loadfile2(filename):
	file = io.open(filename,'r')
	content = file.readlines()
	point = []
	#for i in range(len(content)):
	for j in content:
		index = 1
		if j[0:1]=="s":
			m=j.split()
			point.append(int(m[1]))
	part1_100_10 = []
	part1_100_15 = []
	part1_100_20 = []
	part1_300_10 = []
	part1_300_15 = []
	part1_300_20 = []
	part1_500_10 = []
	part1_500_15 = []
	part1_500_20 = []
	part1_100_50 = []
	part1_100_100 = []
	part1_300_50 = []
	part1_300_100 = []
	part1_500_50 = []
	part1_500_100 = []
	for x in range(19):
		part1_100_10.append(point[x])
	for x in range(19, 38):
		part1_100_15.append(point[x])
	for x in range(38, 38+19):
		part1_100_20.append(point[x])
	for x in range(38+19, 38+19*2):
		part1_300_10.append(point[x])
	for x in range(38+19*2, 38+19*3):
		part1_300_15.append(point[x])
	for x in range(38+19*3, 38+19*4):
		part1_300_20.append(point[x])
	for x in range(38+19*4, 38+19*5):
		part1_500_10.append(point[x])
	for x in range(38+19*5, 38+19*6):
		part1_500_15.append(point[x])
	for x in range(38+19*6, 38+19*7):
		part1_500_20.append(point[x])
	for x in range(38+19*7, 38+19*8):
		part1_100_50.append(point[x])
	for x in range(38+19*8, 38+19*9):
		part1_100_100.append(point[x])
	for x in range(38+19*9, 38+19*10):
		part1_300_50.append(point[x])
	for x in range(38+19*10, 38+19*11):
		part1_300_100.append(point[x])
	for x in range(38+19*11, 38+19*12):
		part1_500_50.append(point[x])
	for x in range(38+19*12, 38+19*13):
		part1_500_100.append(point[x])
	#point1=[]
	#point1.append([])
	xaxis=[]
	for x in range(1, 20):
		xaxis.append(int(x))
	plt.scatter(xaxis, part1_300_10, c='r', marker='o')
	plt.scatter(xaxis, part1_300_50, c='g', marker='x')
	plt.scatter(xaxis, part1_300_100, c='b', marker='*')
	plt.xlim([0,20])
	plt.xlabel('Game number')
	plt.ylabel('Score')
	plt.xticks(range(len(xaxis)+2))
	plt.title('Performance of SARSA with learning trial = 300')
	plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	plt.savefig("Performance of SARSA(POINT).jpg")
	#point = []
	#for i in range()
	#	line1 = content[3+ 3*i].split()
	#	point.append(line1[1])
loadfile2("./results/SARSAResult.txt")

def loadfile2(filename):
	file = io.open(filename,'r')
	content = file.readlines()
	point = []
	#for i in range(len(content)):
	for j in content:
		index = 1
		if j[0:1]=="s":
			m=j.split()
			point.append(int(m[1]))
	part1_100_10 = []
	part1_100_15 = []
	part1_100_20 = []
	part1_300_10 = []
	part1_300_15 = []
	part1_300_20 = []
	part1_500_10 = []
	part1_500_15 = []
	part1_500_20 = []
	part1_100_50 = []
	part1_100_100 = []
	part1_300_50 = []
	part1_300_100 = []
	part1_500_50 = []
	part1_500_100 = []
	for x in range(19):
		part1_100_10.append(point[x])
	for x in range(19, 38):
		part1_100_15.append(point[x])
	for x in range(38, 38+19):
		part1_100_20.append(point[x])
	for x in range(38+19, 38+19*2):
		part1_300_10.append(point[x])
	for x in range(38+19*2, 38+19*3):
		part1_300_15.append(point[x])
	for x in range(38+19*3, 38+19*4):
		part1_300_20.append(point[x])
	for x in range(38+19*4, 38+19*5):
		part1_500_10.append(point[x])
	for x in range(38+19*5, 38+19*6):
		part1_500_15.append(point[x])
	for x in range(38+19*6, 38+19*7):
		part1_500_20.append(point[x])
	for x in range(38+19*7, 38+19*8):
		part1_100_50.append(point[x])
	for x in range(38+19*8, 38+19*9):
		part1_100_100.append(point[x])
	for x in range(38+19*9, 38+19*10):
		part1_300_50.append(point[x])
	for x in range(38+19*10, 38+19*11):
		part1_300_100.append(point[x])
	for x in range(38+19*11, 38+19*12):
		part1_500_50.append(point[x])
	for x in range(38+19*12, 38+19*13):
		part1_500_100.append(point[x])
	#point1=[]
	#point1.append([])
	xaxis=[]
	for x in range(1, 20):
		xaxis.append(int(x))
	plt.scatter(xaxis, part1_300_10, c='r', marker='o')
	plt.scatter(xaxis, part1_300_50, c='g', marker='x')
	plt.scatter(xaxis, part1_300_100, c='b', marker='*')
	plt.xlim([0,20])
	plt.xlabel('Game number')
	plt.ylabel('Score')
	plt.xticks(range(len(xaxis)+2))
	plt.title('Performance of MC with learning trial = 300')
	plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	plt.savefig("Performance of MC(POINT).jpg")
	#point = []
	#for i in range()
	#	line1 = content[3+ 3*i].split()
	#	point.append(line1[1])
loadfile2("./results/MCResult2.txt")
'''

def loadfile(filename):
	file = io.open(filename,'r')
	content = file.readlines()
	point = []
	#for i in range(len(content)):
	for j in content:
		index = 1
		if j[0:1]=="s":
			m=j.split()
			point.append(int(m[1]))
	part1_100_10 = []
	part1_100_15 = []
	part1_100_20 = []
	part1_300_10 = []
	part1_300_15 = []
	part1_300_20 = []
	part1_500_10 = []
	part1_500_15 = []
	part1_500_20 = []
	part1_100_50 = []
	part1_100_100 = []
	part1_300_50 = []
	part1_300_100 = []
	part1_500_50 = []
	part1_500_100 = []
	for x in range(19):
		part1_100_10.append(point[x])
	for x in range(19, 38):
		part1_100_15.append(point[x])
	for x in range(38, 38+19):
		part1_100_20.append(point[x])
	for x in range(38+19, 38+19*2):
		part1_300_10.append(point[x])
	for x in range(38+19*2, 38+19*3):
		part1_300_15.append(point[x])
	for x in range(38+19*3, 38+19*4):
		part1_300_20.append(point[x])
	for x in range(38+19*4, 38+19*5):
		part1_500_10.append(point[x])
	for x in range(38+19*5, 38+19*6):
		part1_500_15.append(point[x])
	for x in range(38+19*6, 38+19*7):
		part1_500_20.append(point[x])
	for x in range(38+19*7, 38+19*8):
		part1_100_50.append(point[x])
	for x in range(38+19*8, 38+19*9):
		part1_100_100.append(point[x])
	for x in range(38+19*9, 38+19*10):
		part1_300_50.append(point[x])
	for x in range(38+19*10, 38+19*11):
		part1_300_100.append(point[x])
	for x in range(38+19*11, 38+19*12):
		part1_500_50.append(point[x])
	for x in range(38+19*12, 38+19*13):
		part1_500_100.append(point[x])
	#point1=[]
	#point1.append([])
	xaxis=[]
	for x in range(1, 20):
		xaxis.append(int(x))
	plt.scatter(xaxis, part1_100_10, c='r', marker='o')
	plt.scatter(xaxis, part1_100_50, c='g', marker='x')
	plt.scatter(xaxis, part1_100_100, c='b', marker='*')
	plt.xlim([0,20])
	plt.xlabel('Game number')
	plt.ylabel('Score')
	plt.xticks(range(len(xaxis)+2))
	plt.title('Performance of UCT with learning trial = 100')
	plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	plt.savefig("Performance of UCT(POINT100).jpg")
	#plt.scatter(xaxis, part1_300_10, c='r', marker='o')
	#plt.scatter(xaxis, part1_300_50, c='g', marker='x')
	#plt.scatter(xaxis, part1_300_100, c='b', marker='*')
	#plt.xlim([0,20])
	#plt.xlabel('game number')
	#plt.ylabel('Score')
	#plt.xticks(range(len(xaxis)+2))
	#plt.title('Performance of UCT with learning trial = 300')
	#plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	#plt.savefig("Performance of UCT(POINT).jpg")
	#point = []
	#for i in range()
	#	line1 = content[3+ 3*i].split()
	#	point.append(line1[1])

loadfile("./results/UCTResult.txt")

'''
from matplotlib import pyplot as plt
import io

def loadfile2(filename):
	file = io.open(filename,'r')
	content = file.readlines()
	point = []
	#for i in range(len(content)):
	for j in content:
		index = 1
		if j[0:1]=="s":
			m=j.split()
			point.append(int(m[1]))
	part1_100_10 = []
	part1_100_15 = []
	part1_100_20 = []
	part1_300_10 = []
	part1_300_15 = []
	part1_300_20 = []
	part1_500_10 = []
	part1_500_15 = []
	part1_500_20 = []
	part1_100_50 = []
	part1_100_100 = []
	part1_300_50 = []
	part1_300_100 = []
	part1_500_50 = []
	part1_500_100 = []
	for x in range(19):
		part1_100_10.append(point[x])
	for x in range(19, 38):
		part1_100_15.append(point[x])
	for x in range(38, 38+19):
		part1_100_20.append(point[x])
	for x in range(38+19, 38+19*2):
		part1_300_10.append(point[x])
	for x in range(38+19*2, 38+19*3):
		part1_300_15.append(point[x])
	for x in range(38+19*3, 38+19*4):
		part1_300_20.append(point[x])
	for x in range(38+19*4, 38+19*5):
		part1_500_10.append(point[x])
	for x in range(38+19*5, 38+19*6):
		part1_500_15.append(point[x])
	for x in range(38+19*6, 38+19*7):
		part1_500_20.append(point[x])
	for x in range(38+19*7, 38+19*8):
		part1_100_50.append(point[x])
	for x in range(38+19*8, 38+19*9):
		part1_100_100.append(point[x])
	for x in range(38+19*9, 38+19*10):
		part1_300_50.append(point[x])
	for x in range(38+19*10, 38+19*11):
		part1_300_100.append(point[x])
	for x in range(38+19*11, 38+19*12):
		part1_500_50.append(point[x])
	for x in range(38+19*12, 38+19*13):
		part1_500_100.append(point[x])
	#point1=[]
	#point1.append([])
	xaxis=[]
	for x in range(1, 20):
		xaxis.append(int(x))
	plt.scatter(xaxis, part1_100_10, c='r', marker='o')
	plt.scatter(xaxis, part1_100_50, c='g', marker='x')
	plt.scatter(xaxis, part1_100_100, c='b', marker='*')
	plt.xlim([0,20])
	plt.xlabel('Game number')
	plt.ylabel('Score')
	plt.xticks(range(len(xaxis)+2))
	plt.title('Performance of q_learning with learning trial = 100')
	plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	plt.savefig("Performance of q_learning(POINT100).jpg")
	#point = []
	#for i in range()
	#	line1 = content[3+ 3*i].split()
	#	point.append(line1[1])

loadfile2("./results/QLResult.txt")
'''
'''
def loadfile3(filename):
	file = io.open(filename,'r')
	content = file.readlines()
	point = []
	#for i in range(len(content)):
	for j in content:
		index = 1
		if j[0:1]=="s":
			m=j.split()
			point.append(int(m[1]))
	part1_100_10 = []
	part1_100_15 = []
	part1_100_20 = []
	part1_300_10 = []
	part1_300_15 = []
	part1_300_20 = []
	part1_500_10 = []
	part1_500_15 = []
	part1_500_20 = []
	part1_100_50 = []
	part1_100_100 = []
	part1_300_50 = []
	part1_300_100 = []
	part1_500_50 = []
	part1_500_100 = []
	for x in range(19):
		part1_100_10.append(point[x])
	for x in range(19, 38):
		part1_100_15.append(point[x])
	for x in range(38, 38+19):
		part1_100_20.append(point[x])
	for x in range(38+19, 38+19*2):
		part1_300_10.append(point[x])
	for x in range(38+19*2, 38+19*3):
		part1_300_15.append(point[x])
	for x in range(38+19*3, 38+19*4):
		part1_300_20.append(point[x])
	for x in range(38+19*4, 38+19*5):
		part1_500_10.append(point[x])
	for x in range(38+19*5, 38+19*6):
		part1_500_15.append(point[x])
	for x in range(38+19*6, 38+19*7):
		part1_500_20.append(point[x])
	for x in range(38+19*7, 38+19*8):
		part1_100_50.append(point[x])
	for x in range(38+19*8, 38+19*9):
		part1_100_100.append(point[x])
	for x in range(38+19*9, 38+19*10):
		part1_300_50.append(point[x])
	for x in range(38+19*10, 38+19*11):
		part1_300_100.append(point[x])
	for x in range(38+19*11, 38+19*12):
		part1_500_50.append(point[x])
	for x in range(38+19*12, 38+19*13):
		part1_500_100.append(point[x])
	#point1=[]
	#point1.append([])
	xaxis=[]
	for x in range(1, 20):
		xaxis.append(int(x))
	plt.scatter(xaxis, part1_100_10, c='r', marker='o')
	plt.scatter(xaxis, part1_100_50, c='g', marker='x')
	plt.scatter(xaxis, part1_100_100, c='b', marker='*')
	plt.xlim([0,20])
	plt.xlabel('Game number')
	plt.ylabel('Score')
	plt.xticks(range(len(xaxis)+2))
	plt.title('Performance of SARSA with learning trial = 100')
	plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	plt.savefig("Performance of SARSA(POINT100).jpg")
	#point = []
	#for i in range()
	#	line1 = content[3+ 3*i].split()
	#	point.append(line1[1])
loadfile3("./results/SARSAResult.txt")
'''
'''
def loadfile4(filename):
	file = io.open(filename,'r')
	content = file.readlines()
	point = []
	#for i in range(len(content)):
	for j in content:
		index = 1
		if j[0:1]=="s":
			m=j.split()
			point.append(int(m[1]))
	part1_100_10 = []
	part1_100_15 = []
	part1_100_20 = []
	part1_300_10 = []
	part1_300_15 = []
	part1_300_20 = []
	part1_500_10 = []
	part1_500_15 = []
	part1_500_20 = []
	part1_100_50 = []
	part1_100_100 = []
	part1_300_50 = []
	part1_300_100 = []
	part1_500_50 = []
	part1_500_100 = []
	for x in range(19):
		part1_100_10.append(point[x])
	for x in range(19, 38):
		part1_100_15.append(point[x])
	for x in range(38, 38+19):
		part1_100_20.append(point[x])
	for x in range(38+19, 38+19*2):
		part1_300_10.append(point[x])
	for x in range(38+19*2, 38+19*3):
		part1_300_15.append(point[x])
	for x in range(38+19*3, 38+19*4):
		part1_300_20.append(point[x])
	for x in range(38+19*4, 38+19*5):
		part1_500_10.append(point[x])
	for x in range(38+19*5, 38+19*6):
		part1_500_15.append(point[x])
	for x in range(38+19*6, 38+19*7):
		part1_500_20.append(point[x])
	for x in range(38+19*7, 38+19*8):
		part1_100_50.append(point[x])
	for x in range(38+19*8, 38+19*9):
		part1_100_100.append(point[x])
	for x in range(38+19*9, 38+19*10):
		part1_300_50.append(point[x])
	for x in range(38+19*10, 38+19*11):
		part1_300_100.append(point[x])
	for x in range(38+19*11, 38+19*12):
		part1_500_50.append(point[x])
	for x in range(38+19*12, 38+19*13):
		part1_500_100.append(point[x])
	#point1=[]
	#point1.append([])
	xaxis=[]
	for x in range(1, 20):
		xaxis.append(int(x))
	plt.scatter(xaxis, part1_100_10, c='r', marker='o')
	plt.scatter(xaxis, part1_100_50, c='g', marker='x')
	plt.scatter(xaxis, part1_100_100, c='b', marker='*')
	plt.xlim([0,20])
	plt.xlabel('Game number')
	plt.ylabel('Score')
	plt.xticks(range(len(xaxis)+2))
	plt.title('Performance of MC with learning trial = 100')
	plt.legend(['Limited step = 10', 'Limited step = 50', 'Limited step = 100'])
	plt.savefig("Performance of MC(POINT100).jpg")
	#point = []
	#for i in range()
	#	line1 = content[3+ 3*i].split()
	#	point.append(line1[1])
loadfile4("./results/MCResult2.txt")
'''