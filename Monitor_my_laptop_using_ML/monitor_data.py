"""
plot static graph: cpu %utilization
"""
import psutil
import time
import os
import numpy as np
import matplotlib.pyplot as plt

"""
Get CPU %utilization and memory %utilization from the system. 
Add 1 if the computer is abnormal, add 0 if normal. 
Save data to a file
Get data every interval seconds, stop when tol_time is using up
"""
def fetchData(fileName, interval, tol_time):
	t = round(tol_time/interval);
	var = 0
	dataFile = open(fileName,'w')
	dataFile.write('')
	dataFile.close()
	dataFile = open(fileName,'a')

	stime = round(time.time())

	while var <= t:
		cpu = psutil.cpu_percent(interval=None)
		dataFile.write(str(cpu))
		dataFile.write(',')
		memory = psutil.virtual_memory().percent
		dataFile.write(str(memory))
		dataFile.write(',')
		if cpu > 70:
			dataFile.write('1') #abnormal
		elif memory > 72:
			dataFile.write('1') #abnormal
		else:
			dataFile.write('0') #normal
		
		dataFile.write('\n')
		time.sleep(interval)
		var = var+1;
		
	dataFile.close()
	
# fetch cpu utilization percentage data every 2 seconds in 2 minutes
fetchData('percent_data.txt', 2, 1200)
