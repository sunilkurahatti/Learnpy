import json
with open('new.txt','r+') as n:
	for i in n:
		# print(i)
		with open('new_write.txt','a') as w:		
			print(i, end='')
			w.writelines(i)
