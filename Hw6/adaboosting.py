from numpy import matrix
from math import log
def sign(x):
		return 1 if x>=0 else -1

x=[]
y=[]
with open('hw6_train.dat','r') as f:
		for line in f:
				tmp=line.split()
				tmp=[float(i) for i in tmp]
				x.append(tmp[0:len(tmp)-1])
				y.append(tmp[len(tmp)-1])
x_m=matrix(x)
y_m=matrix(x)
N=len(x)
dim=len(x[0])
u=[1/float(N)]*N

def g(s,theta,x):
		return s*sign(x-theta)

def err_weight(s,theta,d):
		count=0
		for i in range(N):
				if g(s,theta,x[i][d]) != y[i]:
						count=count+u[i]
		return count
def cmp_err_w(h,theta,d):
		a=err_weight(1,theta,d)
		b=err_weight(-1,theta,d)
		if a < b:
				if a < h[2]:
						return [[d,theta],1,a]
				else:
						return h
		else:
				if b < h[2]:
						return [[d,theta],-1,b]
				else:
						return h
def best_theta():
		cut=[0,0]  #[dim, theta]
		cut[1]=x[0][0]
		s=1
		e_in=10
		h=[cut,s,e_in] # h fnt & err
		for d in range(dim):
				#choose best g
				for theta in x_m[:,d]:
						h=cmp_err_w(h,theta[0,0],d)
		return h
alpha_l=[]
g_l=[]
loop=300
for T in range(loop):
		print('===========%d=========='%T)
		h=best_theta()
		eps=h[2]/sum(u)
		scaler=((1.0-eps)/(eps))**(0.5)
		#change u_t to u_t+1
		for i in range(N):
				if g(h[1],h[0][1],x[i][h[0][0]]) == y[i]:
						u[i]=u[i]/scaler
				else:
						u[i]=u[i]*scaler
		alpha_l.append(log(scaler))
		g_l.append(h)

def G(x):
		count=0
		for T in range(loop):
				s=g_l[T][1]
				theta=g_l[T][0][1]
				d=g_l[T][0][0]
				count = count + g(s,theta,x[d])
		return sign(count)

#Count e_in & e_out
e_in=0
for i in range(N):
		if G(x[i]) !=  y[i]:
				e_in=e_in+1
e_in=e_in/float(N)

print(e_in)

x_out=[]
y_out=[]
with open('hw6_test.dat','r') as f:
		for line in f:
				tmp=line.split()
				tmp=[float(i) for i in tmp]
				x_out.append(tmp[0:len(tmp)-1])
				y_out.append(tmp[len(tmp)-1])
e_out=0
for i in range(len(x_out)):
		if G(x_out[i]) != y_out[i]:
				e_out=e_out+1
e_out=e_out/float(len(x_out))

print(e_out)
	
