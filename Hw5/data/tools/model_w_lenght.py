from sys import argv
from numpy import array

def length(w):
		x=0.0
		for i in w:
				x=x+(i**2)
		length=x**(0.5)
		return(length)
def data_modify(line):
		x=line.split()
		y=[]
		y.append(x[0])
		for i in x[1:]:
				y.append(i.split(':')[1])
		return [float(i) for i in y]
with open(argv[1],'r') as f:
		i=0
		while(i==0):
				line=f.readline()
				i= (line.strip() == 'SV')
		sv=data_modify(f.readline())
		w=sv[0]*array(sv[1:])
		for line in f:
				sv=data_modify(line)
				w=w+sv[0]*array(sv[1:])
		print(length(w))

		
