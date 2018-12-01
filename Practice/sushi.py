# for i in range(11,20):
# 	print(i)

with open('new.txt','r') as f:
	for lines in f:
		print(lines, end='')