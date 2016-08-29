from sys import argv
import bintrees as bt
model=argv[1]
data_file=argv[2]
#Create data tree for search y_value
d_tree=bt.AVLTree()
with open(data_file,'r') as f:
		for line in f:
				x=line.split()
				v=[]
				for elm in x[1:]:
						v.append(float(elm.split(':')[1]))
				d_tree.insert(v,float(x[0]))

with open(model,'r') as f:
		i=0
		while(i==0):
				line=f.readline()
				i=(line=='SV\n')
		ans=0.0
		for line in f:
				x=line.split()
				v=[]
				for elm in x[1:]:
						a=elm.split(':')[1]
						v.append(float(elm.split(':')[1]))
				y=d_tree.get(v)
				ans=ans+float(x[0])*y
		print(model+' : '+str(ans))
				
