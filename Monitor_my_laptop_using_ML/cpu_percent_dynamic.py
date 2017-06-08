"""
plot dynamic graph: cpu %utilization
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#-----------------------load data------------------------#
def loadData(fileName):
	inFile = open(fileName, 'r')
	#defile 2 empty arrays to store the data
	X = []
	y = []
	for line in inFile:
		trainingSet = line.split(',')
		X.append(trainingSet[0])
		y.append(trainingSet[1])
	return (X, y)
	
(x1, y1) = loadData('cpu_percent_data.txt')
#----------------------load data end---------------------#

#-----------------------plot graph-----------------------#
fig, ax = plt.subplots()
x1 = np.arange(0, 122, 2)
line, = ax.plot(x1, y1)

def animate(i):
	line.set_ydata(y1[i])
	return line,

# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x1, mask=True))
    return line,
ani = animation.FuncAnimation(fig, animate, np.arange(0, 61), init_func=init,
                              interval=25, blit=True)
plt.show()
#---------------------plot graph end----------------------#
















