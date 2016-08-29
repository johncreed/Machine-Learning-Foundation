import os as os
from math import log10
gamma_list=[10000,1000,100,10,1]
select=[0,0,0,0,0]
x=[4,3,2,1,0]
index=dict(zip(gamma_list,x))
path1='~/Desktop/libsvm-3.21/'
path2='~/Desktop/libsvm-3.21/tools/'
path3='~/Desktop/libsvm-3.21/data/format_data/'
path4='~/Desktop/libsvm-3.21/data/Q20/'

for i in range(100):
		os.system(path2+'subset.py -s 1 '+path3+'features_0.train 1000 '+path4+'val_set.dat '+path4+'train_set.dat')
		for gamma in gamma_list: 
				os.system(path1+'svm-train -m 2000  -g '+str(gamma)+' -c 0.1 '+path4+'train_set.dat '+path4+'model > '+path4+'trash.txt')
				os.system(path1+'svm-predict '+path4+'val_set.dat '+path4+'model output >> '+path4+'Accuracy.txt')
		with open('Accuracy.txt','r') as f:
				score_list=[]
				for line in f:
						x=line.split()
						score=float(x[2].rstrip('%'))
						score_list.append(score)
		os.system('rm '+path4+'Accuracy.txt')
		print(score_list)
		dictionary=dict(zip(score_list,gamma_list))
		a=index[dictionary[max(score_list)]]
		select[4-a]=select[4-a]+1
		print(select)

