import psutil
import time
import os

var = 0
dataFile = open('cpu_percent_data.txt','w')
dataFile.write('')
dataFile.close()
dataFile = open('cpu_percent_data.txt','a')

stime = round(time.time())
while var < 100:
	dataFile.write(str(round(time.time())-stime))
	dataFile.write(',')
	dataFile.write(str(psutil.cpu_percent(interval=None)))
	dataFile.write('\n')
	time.sleep(2)
	var = var + 1;
dataFile.close()