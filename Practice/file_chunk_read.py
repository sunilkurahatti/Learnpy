import time
f=open('new.txt','r')
a=time.time()
size=100

pt=f.read(size)
while len(pt) >0:
	print(pt, end='')
	pt=f.readline(size)

print("time take=",time.time()-a)
