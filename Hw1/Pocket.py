#!/usr/local/bin/python3
import numpy as np
import random as rdm
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import time
####    Readiing Data    #####


data = []
data_size = 0


with open( 'hw1_18_train.dat', 'r') as f:
	for line in f:
		x_l = line.split()
		x = x_l[0:4]
		x.append(1)
		x_t = tuple( [np.matrix( x, dtype = 'float64'), float( x_l[4] ) ]  )
		data.append(x_t)
		data_size += 1


data_t = []
answer_t = []
data_t_size = 0


with open( 'hw1_18_test.dat', 'r') as f:
	for line in f:
		x_l = line.split()
		x = x_l[0:4]
		x.append(1)
		data_t.append(x)
		answer_t.append(x_l[4])
		data_t_size +=1

data_t_m = np.matrix(data_t, dtype='float64')
answer_t_m = np.matrix(answer_t, dtype='float64')

####     =============     ####

def sign(x):
	if x > 0:
		return 1
	else:
		return -1


def verify(x,y):
	err_x = 0
	err_y = 0
	
	err_x = ((((data_t_m*x.T) >= 0)*2-1) != answer_t_m.T).sum()
	err_y = ((((data_t_m*y.T) >= 0)*2-1) != answer_t_m.T).sum()
	if err_x <= err_y :
		return tuple( [x, err_x] )
	else:
		return tuple( [y, err_y] )
	
err_all = []
update_limit = 2000
iteration = 200
for a in range(iteration):
	start_time = time.time()

	print('======', a ,'======')
	rdm.shuffle(data)
	flaw = 1
	w = np.matrix([0,0,0,0,0] , dtype = 'float64')
	total_update = 1
	err = 0
	
	total_inspect = 0
	while (total_update < update_limit):
		clear = 0
		for point in data:
			total_inspect += 1

			if sign( point[0] * w.T ) != point[1]:
				k = verify( w + 1 * point[1] * point[0], w)
				w = k[0]
				err = k[1]
				total_update += 1
			else:
				clear += 1
			if total_update == update_limit:
				break

		if clear == data_size:
			break
	print ('total_update : %d' % total_update)
	print ('total_inspect: %d' % total_inspect)
	
	print ('total_time : %s' %(time.time() - start_time))
	err_all.append(err)
	print ('err %d' %err)


err_all_a = []
update_limit = 10

for a in range(iteration):
	start_time = time.time()

	print('======', a ,'======')
	rdm.shuffle(data)
	flaw = 1
	w = np.matrix([0,0,0,0,0] , dtype = 'float64')
	total_update = 1
	err = 0
	
	total_inspect = 0
	while (total_update < update_limit):
		clear = 0
		for point in data:
			total_inspect += 1

			if sign( point[0] * w.T ) != point[1]:
				k = verify( w + 1 * point[1] * point[0], w)
				w = k[0]
				err = k[1]
				total_update += 1
			else:
				clear += 1
			if total_update == update_limit:
				break

		if clear == data_size:
			break
	print ('total_update : %d' % total_update)
	print ('total_inspect: %d' % total_inspect)
	
	print ('total_time : %s' %(time.time() - start_time))
	err_all_a.append(err)
	print ('err %d' %err)
plt.xkcd()
bins = np.linspace(0,200,50)
plt.hist(err_all,bins,alpha=0.5,label='x')
plt.hist(err_all_a,bins,alpha=0.5,label='y')
plt.legend(loc='upper right')
plt.show()
