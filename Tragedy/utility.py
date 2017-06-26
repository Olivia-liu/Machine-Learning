import csv

def get_data(filename):
	#read all columns in X_file
	inFile = open(filename)
	reader = csv.reader(inFile)
	data = list(reader)
	inFile.close()
	return data
	
	
	
	
	
	


