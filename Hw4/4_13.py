# Regularization Linear Regression and Validation
import numpy as np
import matplotlib.pyplot as plt
import math

x = []
y = []
with open('./hw4_train.dat','r') as f:
		for line in f:
				tmp = line.split()
				tmp = [float(i) for i in tmp]
				x.append(np.concatenate(([1],tmp[0:len(tmp)-1])).tolist())
				y.append(tmp[len(tmp)-1])

x_m = np.matrix(x)
y_v = np.matrix(y).T
i = np.identity(x_m.shape[1])
print(x)
x_out =[]
y_out = []
with open('./hw4_test.dat','r') as f:
		for line in f:
				tmp = line.split()
				tmp = [float(i) for i in tmp]
				x_out.append(np.concatenate(([1],tmp[0:len(tmp)-1])).tolist())
				y_out.append(tmp[len(tmp)-1])

x_out_m = np.matrix(x_out)
y_out_v = np.matrix(y_out).T

def sign(x):
		if x > 0 :
			return 0
		else:
			return 1
def err_fnt(w,x_m,y_v):
		y_pre = x_m * w
		z = np.multiply(y_pre,y_v)
		count = 0
		for elm in z:
				count = count + sign(elm[0,0])
		return (1/float(x_m.shape[0]))*count

lmb_arr = [10**i for i in range(-10,5)]
e_in_arr = []
e_out_arr = []
for lmb in lmb_arr:
		#Compute the best w

		w = (lmb*i+x_m.T*x_m).I * (x_m.T*y_v)

		#Calculate e_in and e_out

		e_in_arr.append(err_fnt(w,x_m,y_v))

		e_out_arr.append(err_fnt(w,x_out_m,y_out_v))

plt.plot([i for i in range(-10,5)],e_in_arr,'bo',[i for i in range(-10,5)],e_out_arr,'ro')
plt.show()




