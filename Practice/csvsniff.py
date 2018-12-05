import csv
with open('AAPL.csv','r') as AP_RCSV:
	sn=csv.Sniffer().sniff(AP_RCSV.read(10))
	csv_read=csv.reader(AP_RCSV,sn)
	for l in csv_read:
		print(l)