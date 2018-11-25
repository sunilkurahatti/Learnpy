import csv

cnt=0

while cnt<=30:
	with open('emp.csv','r') as dicr:
		rdic=csv.DictReader(dicr)
		with open('dictwr.csv','a') as dicw:
			fl=['Department','Salary','Manager','Name']
			# fl=[rdic[0],rdic[1],rdic[2],rdic[3]]
			wdic=csv.DictWriter(dicw,fieldnames=fl)
			wdic.writeheader()
			for ln in rdic:
				print(ln['Name'])
				wdic.writerow(ln)
	cnt=cnt+1