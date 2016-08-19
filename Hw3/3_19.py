import numpy as np
import math as mth

#Process data

x = []
y = []

with open('hw3_train.dat', 'r') as f:
		for line in f:
				data = [float(b) for b in line.split()]
				a = [1.0]
				a = np.concatenate((a, data[0:(len(data)-1)])).tolist()
				x.append(a)
				y.append( data[len(data)-1] )

x_m = np.matrix(x)
y_v = np.matrix(y).T
x_row = float(x_m.shape[0])
x_column = float(x_m.shape[1])
print(x_m.shape)
print(y_v.shape)


#Choosing Proper w for Logistic Regression with step eta = 0.001 and T = 2000

eta = 0.01
T = 1000

w = np.matrix( [0] * int(x_column) ).T
def h_funt(x):
		return mth.exp(x)/(1+mth.exp(x))

def gradient_cal(w):
		a = np.matrix( [0] * int(x_column) ).T
		for n in range(int(x_row)):
			b = (-1*y[n]*x_m[n]*w)[0,0]
			h = h_funt(b)
			a = a + h * (-1*y[n]*x_m[n].T)
		print(a)
		return (1/x_row) * a

for loop in range(T):
		print('======== %d =========' %loop)
		w = w - eta * gradient_cal(w)

# Count err 0/1 in test data

x_out = []
y_out = []

with open('hw3_test.dat', 'r') as f:
		for line in f:
				data = [float(b) for b in line.split()]
				a = [1.0]
				a = np.concatenate((a, data[0:(len(data)-1)])).tolist()
				x.append(a)
				y.append( data[len(data)-1] )

x_out_m = np.matrix(x)
y_out_v = np.matrix(y).T


count = 0

ans_m  = np.multiply(y_out_v , (x_out_m * w))

ans = ans_m.T.tolist()[0]
for elm in ans:
		if elm < 0 :
				count = count + 1
	

print(count)

				
