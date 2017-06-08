import psutil
import time
import os
import numpy as np
import matplotlib.pyplot as plt
import numpy as np  
import pandas as pd  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.linear_model.logistic import LogisticRegression  
from sklearn.cross_validation import train_test_split, cross_val_score  


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
	
(X, y) = loadData('cpu_percent_data_logistic.txt')
X_test = [30, 40, 50, 10, 20]

classifier = LogisticRegression()  
classifier.fit(X,y)  
predictions = classifier.predict(X_test)  

for i,predictions in enumerate(predictions[-5:]):  
    print ('Prediction type:%s. Information: %s' %(predictions,X_test_raw.iloc[i]))  
	
#scores = cross_val_score(classifier, X_train, y_train, cv=5)  
#print('Score:',np.mean(scores), scores)  