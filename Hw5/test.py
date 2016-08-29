import urllib.request as req

x = req.urlretrieve('https://tools.ietf.org/html/rfc2616.html')
#print(x)

with open(x[0],'r') as f:
		for line in f:
				print(line)

