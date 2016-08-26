import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix,solvers
x = np.matrix([[1,0],[0,1],[0,-1],[-1,0],[0,2],[0,-2],[-2,0]],dtype=float)
y = np.matrix([-1,-1,-1,1,1,1,1],dtype=float)

def transformation(x):
	for item in x:
		a=item[0,0]
		b=item[0,1]
		item[0,0]=b**2-2*a+3
		item[0,1]=a**2-2*b-3
#transformation(x)
#Plot the Scatter Graph
#plt.plot(x[0:3,0].T.tolist()[0],x[0:3,1].T.tolist()[0],'ro',x[3:,0].T.tolist()[0],x[3:,1].T.tolist()[0],'bo')
#plt.show()
def kernel(a,b):
		return (1+(a*b.T)[0,0])**2

Q = matrix(0.0,(7,7))
for i in range(7):
		for j in range(7):
				Q[i,j] = y[0,i]*y[0,j]*kernel(x[i],x[j])
q = matrix(-1.0,(7,1))
G = matrix(-1.0*np.identity(7,dtype=float))
h = matrix(0.0,(7,1))
A = matrix(y.A)
b = matrix(0.0)

sol = solvers.qp(Q,q,G,h,A,b)

print(sol['x'])
print(sum(sol['x']))
z=[]
for i in range(7):
		a=x[i,0]
		b=x[i,1]
		z.append([1,a,b,2**(1/2)*a*b,a**2,b**2])
print(np.matrix(z))

w = np.matrix(np.array(sol['x']).T*np.array(y)) * z
print(w)

