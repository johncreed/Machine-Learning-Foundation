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

x_fold = []
for i in range(5):
		x_fold.append(x[40*i:40*(i+1)])
y_fold = []
for i in range(5):
		y_fold.append(y[40*i:40*(i+1)])

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
def return_fold(a, fold, t = 0):
		tmp = []
		for i in range(5):
				if i != a:
					tmp.append(fold[i])
		x = np.matrix(np.concatenate(tmp))
		if t == 0:
				return(np.matrix(fold[a]), x)
		else:
				return(np.matrix(fold[a]).T,x.T)
			
def w_cal(lmb,x_m,y_v):
		return (lmb*i+x_m.T*x_m).I * (x_m.T*y_v)


lmb_arr = [10**i for i in range(-10,3)]
err_arr = []
for lmb in lmb_arr:
		err = 0
		for i in range(5):
				x_val_m,x_train_m  = return_fold(i,x_fold)
				y_val_v,y_train_v = return_fold(i,y_fold,1)
				w=w_cal(lmb,x_train_m,y_train_v)
				err = err + err_fnt(w,x_val_m,y_val_v)
		err_arr.append(err/5)

lmb_b = dict(zip(err_arr,lmb_arr))[min(err_arr)]
print(lmb_b)
w=w_cal(lmb_b,x_m,y_v)
print(err_fnt(w,x_out_m,y_out_v))
print(err_fnt(w,x_m,y_v))



