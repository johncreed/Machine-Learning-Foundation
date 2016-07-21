import numpy as np
import time as time
data = []
answer = []

with open('hw1_18_test.dat', 'r') as f:
	for line in f:
		x_l = line.split()
		data.append(x_l[0:4])
		answer.append(x_l[4])

data_m = np.matrix(data,dtype='float64')
answer_m = np.matrix(answer,dtype='float64')
x_v =np.matrix( [1,2,3,4] ).T

start_time = time.time()
(((data_m*x_v >= 0)*2 -1) != answer_m.T ).sum() 

(((data_m*x_v >= 0)*2 -1) != answer_m.T ).sum() 

print (time.time() - start_time)

		
