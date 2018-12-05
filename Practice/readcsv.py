import csv

with open('AAPL.csv','r') as AP_RCSV:
	csv_read=csv.reader(AP_RCSV)
	with open('skaapl.csv','w') as write_csv:
		csv_wirte=csv.writer(write_csv, delimiter='|')
		for line in csv_read:
			csv_wirte.writerow(line)