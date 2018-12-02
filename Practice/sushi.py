# for i in range(11,20):
# 	print(i)

with open('new.txt','r') as f:
	for lines in f:
		ln=str(lines)
		lns=[]
		lns.append(lines)
		lns1=ln.split(' ')
		print(lines, end='')
		print(lns1, end='')
		for i in lns1:
			print(i)