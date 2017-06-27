#-------------- machine learning program STARTS here --------------#
from utility import *
import tensorflow as tf
from numpy.random import RandomState

#-------------- Define some global variables --------------#
age_idx = 2
sex_idx = 1
fare_idx = 5

#-------------- read data from csv files --------------#
X_all = get_data('train_X.csv')
y_all = get_data('train_y.csv')
X_submit = get_data('submit_X.csv')

#-------------- fill empty features, -1 for female, 1 for male --------------#
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
		
for row in X_submit:
	if(row[age_idx] == ''):
		row[age_idx] = str(average_age)
	if(row[sex_idx] == 'female'):
		row[sex_idx] = '-1'
	else:
		row[sex_idx] = '1'
		
#convert lists to arrays
X_all = np.array(X_all, dtype = float)
y_all = np.array(y_all, dtype = float)
X_submit = np.array(X_submit, dtype = float)
		
#-------------- split train, cross-validation and test sets --------------#
X_train = X_all[0:891]
y_train = y_all[0:891]
dataset_size = 891


X_val = X_all[534:712]
y_val = y_all[534:712]

X_test = X_all[712:891]
y_test = y_all[712:891]

#-------------- normalize the training set --------------#
normalize(X_train, age_idx)
normalize(X_train, fare_idx)
normalize(X_submit, age_idx)
normalize(X_submit, fare_idx)

import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
for row in X_submit:
	outputWriter.writerow(row)
outputFile.close()

#print(y_train)
#-------------- Tensorflow to calculate weights STARTS --------------#
batch_size = 8

# define neural network parameters (weights)
w1 = tf.Variable(tf.random_normal([6,12], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([12,12], stddev=1, seed=1))
w3 = tf.Variable(tf.random_normal([12,1], stddev=1, seed=1))
biases1 = tf.Variable(tf.constant(0.1, shape=[12]))
biases2 = tf.Variable(tf.constant(0.1, shape=[12]))
biases3 = tf.Variable(tf.constant(0.1, shape=[1]))

# Use none for small batch
x = tf.placeholder(tf.float32, shape=(None, 6), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

# define forward propagation(sigmoid)
a1 = tf.sigmoid(tf.matmul(x, w1)+biases1)
a2 = tf.sigmoid(tf.matmul(a1, w2)+biases2)
y = tf.sigmoid(tf.matmul(a2, w3)+biases3)

# define cost function and back propagation algorithm
cross_entropy = tf.reduce_mean(
	-y_*tf.log(tf.clip_by_value(y, 1e-10, 1.0)) - (1-y_)*tf.log(tf.clip_by_value(1-y, 1e-10, 1.0)))
#cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_)
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

# create a session
with tf.Session() as sess:
	init_op = tf.initialize_all_variables()
	sess.run(init_op)

	STEPS = 30000
	for i in range(STEPS):
		start = (i * batch_size) % dataset_size
		end = min(start+batch_size, dataset_size)
		
		sess.run(train_step,
				feed_dict={x: X_train[start:end], y_: y_train[start:end]})
		if i%1000 == 0:
			total_cross_entropy = sess.run(
				cross_entropy, feed_dict={x: X_train, y_: y_train})
			#print("After %d training steps, cross entropy on all data is %g" %
				#(i, total_cross_entropy))
			
	#print(sess.run(
	#			cross_entropy, feed_dict={x: X_val, y_: y_val}))		
	#print(sess.run(
	#			cross_entropy, feed_dict={x: X_test, y_: y_test}))					
	print(sess.run(w1))
	print(sess.run(w2))
	print(sess.run(w3))
	
	print(biases1.eval())
	print(biases2.eval())
	print(biases3.eval())
	
	#weight1 = sess.run(w1)
	#weight2 = sess.run(w2)
	
	#prediction = y
	#print ("predictions", prediction.eval(feed_dict={x: X_train, y_: y_train}, session=sess))
	#print(y_train)
	

#-------------- Tensorflow to calculate weights ENDS --------------#

#-------------- calculate predictions --------------#



#-------------- machine learning program ENDS here --------------#
	


