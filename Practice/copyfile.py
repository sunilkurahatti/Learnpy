import time

a=time.time()


with open('22.png','rb') as rf:
	with open('mine.png','wb') as wf:
		for line in rf:
			wf.write(line)
	with open('mine.pdf','wb') as wpdf:
		wpdf.write(line)

print("time take=",time.time()-a)