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

x_train_m = np.matrix(x[0:120])
y_train_v = np.matrix(y[0:120]).T
i = np.identity(x_train_m.shape[1])

x_val = x[120:200]
y_val = y[120:200]
x_val_m = np.matrix(x_val)
y_val_v = np.matrix(y_val).T

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

lmb_arr = [10**i for i in range(-10,3)]
'''
lmb_arr = []
for i in range(10000):
	lmb_arr.append(0.0001*i)
'''
e_train_arr = []
e_val_arr = []
e_out_arr = []

count = 0
for lmb in lmb_arr:
		count = count + 1
		print(count)
		#Compute the best w

		w = (lmb*i+x_train_m.T*x_train_m).I * (x_train_m.T*y_train_v)

		#Calculate e_in and e_out

		e_train_arr.append(err_fnt(w,x_train_m,y_train_v))
		e_val_arr.append(err_fnt(w,x_val_m,y_val_v))
		e_out_arr.append(err_fnt(w,x_out_m,y_out_v))

x_axis =  [i for i in range(-10,3)]
plt.plot(x_axis,e_train_arr,'bo',x_axis,e_val_arr,'ro',x_axis,e_out_arr,'go')
#plt.show()

total = [e_train_arr,e_val_arr,e_out_arr]
print(np.matrix(total).T)

d = dict(zip(e_val_arr,lmb_arr))
lmb = d[max(e_val_arr)]
w = (lmb*i+x_m.T*x_m).I * (x_m.T*y_v)
print(err_fnt(w,x_m,y_v))
print(err_fnt(w,x_out_m,y_out_v))




