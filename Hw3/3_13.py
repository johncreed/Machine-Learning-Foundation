import numpy as np
import matplotlib.pyplot as plt
import random as rnd
def sign(x):
	if x >= 0:
		return 1
	else:
		return 0

hist_data = []
hist_transform_data = []

for loop in range(1):

	print('===========%d============' %loop)

	# Gernerating data set: uniform x = [-1,1]x[-1,1],  N = 1000
	data = []

	for _ in range(10):
		data.append([float(1),rnd.uniform(-1,1), rnd.uniform(-1,1)])

	data_m = np.matrix(data)

	def target_function(x):
		flip = rnd.uniform(0,10)
		if flip >= 1:
			return sign(x[1]**2 + x[2]**2 -0.6)
		else:
			return -sign(x[1]**2 + x[2]**2 -0.6)

	y = []
	for x in data:
		y.append(target_function(x))
	y_v = np.matrix(y).T

	# Withoust non-Linear Transformation:
	
	data_square = data_m.T * data_m
	w = data_square.I * data_m.T * y_v

	#count err0/1
	count = 0
	for x in range(data_m.shape[0]):
		if sign(data_m[x] * w) != y_v[x]:
			count = count + 1

	hist_data.append(count)

	#With non-linear Transformation
	
	x1_square_nda = np.square(data_m[:,1])
	x2_square_nda = np.square(data_m[:,2])
	x1_multi_x2_nda = np.multiply( np.asarray(data_m[:,1]) , np.asarray(data_m[:,2]))

	data_tran_m =  np.asmatrix(np.concatenate((data_m,x1_square_nda,x2_square_nda,x1_multi_x2_nda), axis=1))
	print('data_tran_m')
	print(data_tran_m)

	print(data_tran_m)	

plt.hist(hist_data)
plt.show()


