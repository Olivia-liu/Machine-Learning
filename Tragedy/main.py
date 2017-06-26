from utility import *

age_idx = 2
sex_idx = 1
fare_idx = 5
###---read data from csv files---###
X_all = get_data('train_X.csv')
y_all = get_data('train_y.csv')

###---normalize features---###
total_age = 0
num_people = 0
#calculate average age
for row in X_all:
	if(row[age_idx] != ''):
		total_age = total_age + float(row[age_idx])
		num_people = num_people + 1
average_age = total_age/num_people
#fill empty ages with the average age
#set female to be -1, male to be 1
for row in X_all:
	if(row[age_idx] == ''):
		row[age_idx] = str(average_age)
	if(row[sex_idx] == 'female'):
		row[sex_idx] = '-1'
	else:
		row[sex_idx] = '1'
		

		
###---split train, cross-validation and test sets---###
X_train = X_all[0:534]
y_train = y_all[0:534]

X_val = X_all[534:712]
y_val = y_all[534:712]

X_test = X_all[712:891]
y_test = y_all[712:891]


