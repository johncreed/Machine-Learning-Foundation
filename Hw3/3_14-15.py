import random as rnd
import numpy as np
import matplotlib.pyplot as plt

def sign(x):
		if x >= 0:
				return float(1)
		else:
				return float(-1)
def target_function(x):
		flip = rnd.uniform(0,10)
		if flip >= 1:
				return sign(x[1]**2 + x[2]**2 -0.6)
		else:
				return -sign(x[1]**2 + x[2]**2 -0.6)
data_size = 10000

data_out = []
#Gernerating out  data
for _ in range(data_size):
		a = rnd.uniform(-1,1)
		b = rnd.uniform(-1,1)
		data_out.append([1,a,b,a*b,a**2,b**2])

y_out = []

for x in data_out:
		y_out.append(target_function(x))

data_out_m = np.matrix(data_out)
y_out_v = np.matrix(y_out).T

hist_data = []
hist_data_out = []

for loop in range(100):
		print('============%d============' % loop)
		data = []
		#Gernerating data
		for _ in range(data_size):
				a = rnd.uniform(-1,1)
				b = rnd.uniform(-1,1)
				data.append([1,a,b,a*b,a**2,b**2])

		y = []

		for x in data:
				y.append(target_function(x))

		data_m = np.matrix(data)
		y_v = np.matrix(y).T

		#Calculation w and err0/1
		data_square_m =  data_m.T * data_m
		w = data_square_m.I * data_m.T * y_v

		count_in = 0
		count_out = 0

		for x in range(data_size):
				if sign(data_m[x] * w) != y_v[x] :
						count_in = count_in + 1
				if sign(data_out_m[x] * w) != y_out_v[x]:
						count_out = count_out + 1

		hist_data.append(count_in)
		hist_data_out.append(count_out)
		
plt.hist([hist_data,hist_data_out], label = ['hist_data', 'hist_data_out'])
plt.legend()
plt.show()




