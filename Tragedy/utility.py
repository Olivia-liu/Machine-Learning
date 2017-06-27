import csv
import numpy as np

def get_data(filename):
	#read all columns in X_file
	inFile = open(filename)
	reader = csv.reader(inFile)
	data = list(reader)
	inFile.close()
	return data
	
#return new column
def normalize(data, col):
	#calculate average
	sum = 0
	num = 0
	for row in data:
		sum = sum + row[col]
		num = num + 1
	average = sum/num
	
	#calculate standard deviation
	sum2 = 0
	for row in data:
		sum2 = sum2 + (row[col] - average)**2
	std = (sum2/num)**0.5
	
	for row in data:
		row[col] = (row[col] - average)/std
	
	
	
	
	
	
	
	


