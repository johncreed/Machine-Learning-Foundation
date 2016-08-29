from sys import argv

name = argv[1].split('.')
num = int(argv[2])

with open(name[0]+'_'+str(num)+'.'+ name[1],'w') as f1:
		with open(name[0]+'.'+name[1],'r') as f2:
				for line in f2:
						x=line.split()
						if float(x[0]) == num:
								f1.write('+1 1:'+x[1]+' 2:'+x[2]+'\n')
						else:
								f1.write('-1 1:'+x[1]+' 2:'+x[2]+'\n')


