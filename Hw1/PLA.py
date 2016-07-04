import numpy as np
import random as rdm

f = open( 'data.txt', 'r' )

data = []
data_size = 0

for line in f:
	x_l = line.split()
	x = x_l[0:4]
	x.append(1)
	x_t = tuple( [np.matrix( x, dtype = 'float64'), float( x_l[4] ) ]  )
	data.append(x_t)
	data_size += 1


def sign (x):
	if x > 0:
		return 1
	else:
		return -1

sum_step = 0

for a in range(2000):
	print('======', a ,'======')
	rdm.shuffle(data)
	flaw = 1
	w = np.matrix([0,0,0,0,0] , dtype = 'float64')
	total = 0

	while (flaw == 1) :
		total += 1
		count = 0
		for point in data:
			if sign( point[0] * w.T ) != point[1]:
				w = w + 0.5 * point[1] * point[0]
			else:
				count = count + 1
		if count == data_size:
			flaw = 0
	print(total)
	sum_step += total
	print(sum_step)

print (sum_step/2000)
