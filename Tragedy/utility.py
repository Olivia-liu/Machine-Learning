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
def normalize(X, col):
	#calculate average
	
	#calculate standard deviation
	
	
	
	
	


