# with open('mine.txt','rb') as rt:
# 	with open('jpg.png','wb') as wp:
# 		for line in rt:
# 			wp.write(line)

import time
f=open('22.png','rb')
wf=open('333.png','wb')
a=time.time()
size=100000

pt=f.read(size)
while len(pt) >0:
	# print(pt, end='')
	wf.write(pt)
	pt=f.read(size)
f.close()
wf.close()
print("time take=",time.time()-a)
