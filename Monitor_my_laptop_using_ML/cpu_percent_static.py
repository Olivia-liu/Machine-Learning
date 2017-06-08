"""
plot static graph: cpu %utilization
"""
import psutil
import time
import os
import numpy as np
import matplotlib.pyplot as plt

#get CPU %utilization from the system and save the data in a file
#get data every interval seconds, stop when tol_time is using up
def fetchCPUPercent(fileName, interval, tol_time):
	t = round(tol_time/interval);
	var = 0
	dataFile = open(fileName,'w')
	dataFile.write('')
	dataFile.close()
	dataFile = open(fileName,'a')

	stime = round(time.time())

	while var <= t:
		dataFile.write(str(round(time.time())-stime))
		dataFile.write(',')
		dataFile.write(str(psutil.cpu_percent(interval=None)))
		dataFile.write('\n')
		time.sleep(interval)
		var = var+1;
		
	dataFile.close()

#read the saved data from cpu_percent_data.txt to 2 arrays
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
	
def plotData(X, y):
	plt.plot(X, y)
	plt.ylabel('CPU utilization(%)') 
	plt.xlabel('second(s)')
	plt.title('CPU %utilization changes over time')  
	plt.show()

# fetch cpu utilization percentage data every 2 seconds in 2 minutes
#fetchCPUPercent('cpu_percent_data.txt', 2, 120)
(X, y) = loadData('cpu_percent_data.txt')
plotData(X, y)