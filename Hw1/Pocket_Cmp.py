import numpy as np
import random as rdm
import plotly.plotly as py
import plotly.graph_objs as go

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
data_t_size = 0


with open( 'hw1_18_test.dat', 'r') as f:
	for line in f:
		x_l = line.split()
		x = x_l[0:4]
		x.append(1)
		x_t = tuple( [np.matrix( x, dtype = 'float64'), float( x_l[4] ) ] )
		data_t.append(x_t)
		data_t_size +=1

####     =============     ####

def sign(x):
	if x > 0:
		return 1
	else:
		return -1


def verify(x,y):
	err_x = 0
	err_y = 0
	
	for i in range(data_t_size):
		if sign(x*data_t[i][0].T) != data_t[i][1] :
			err_x += 1
		if sign(y*data_t[i][0].T) != data_t[i][1] :
			err_y +=1

	if err_x >= err_y :
		return tuple( [x, err_x] )
	else:
		return tuple( [y, err_y] )
	
err_all = []

for a in range(1):
	print('======', a ,'======')
	rdm.shuffle(data)
	flaw = 1
	w = np.matrix([0,0,0,0,0] , dtype = 'float64')
	total_update = 1
	err = 0
	
	total_inspect = 0
	while (total_update < 50):
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
			if total_update == 50:
				break
			
		print ('total_update : %d' % total_update)
		print ('total_inspect: %d' % total_inspect)
		if clear == data_size:
			break

	err_all.append(err)
	print ('err %d' %err)


data_his = [ go.Histogram(x = err_all ) ]

fig = go.Figure(data=data_his)
py.iplot( fig, filename =  'Pocket 2000 Q18' )


