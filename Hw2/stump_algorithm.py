import numpy as np
import random as rd
import matplotlib.pyplot as plt
import time

def sign(x):
	if x >= 0:
		return 1
	else:
		return -1

def h_fnt(x,theta):
	return sign(x-theta)

def e_out_fnt(theta):
	return abs(theta)/2 

err_in_list = []
err_out_list = []
theta_list = []
times = 5000
data_size = 20

for now in range(times):
	print('======= %d ==========' %now)
	start_t = time.time()
	x = np.random.uniform(-1,1,data_size)
	
	tmp = []
	for item in x:
		noise = rd.randint(1,5)
		if item > 0:
			if noise >=2:
				tmp.append(1)
			else:
				tmp.append(-1)
		else:
			if noise >=2:
				tmp.append(-1)
			else:
				tmp.append(1)

	y = np.array(tmp)



	err_in = 0
	theta = 0
	start = 0
	for a in x:
		err = 0
		for idx,item in enumerate(x):
			if h_fnt(item,a) != y[idx]:
				err +=1
		if start == 0:
			err_in = err
			theta = a
			start += 1
		elif err_in > err:
			err_in = err
			theta = a
	
	err_in_list.append(float(err_in)/data_size)
	theta_list.append(theta)
	
for item in theta_list:
	err_out_list.append(e_out_fnt(item))


space = np.linspace(-1,1,50)
diff = np.array(err_in_list)-np.array(err_out_list)
plt.hist(diff,bins = space, alpha=0.5,label='diff')
plt.hist(err_in_list, bins = space, alpha=0.5,label='e_in')
plt.hist(err_out_list , bins = space, alpha=0.5, label='e_out')
plt.legend()
plt.show()

