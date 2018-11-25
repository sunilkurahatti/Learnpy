import csv

with open('emp.csv','r') as cv:
	sv=csv.reader(cv)
	with open('new.csv','a') as cw:

		for line in sv:
			print(line)
			rw=csv.writer(cw, delimiter='|')
			rw.writerow(line)