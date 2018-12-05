import csv

with open('AAPL.csv','r') as csv_r:
	csv_read=csv.DictReader(csv_r)
	with open('sundictcsv.csv','w') as csv_w:
		fn=['Date','Open','Low','Close','Adj Close','Volume']
		csv_write=csv.DictWriter(csv_w, fieldnames=fn, delimiter='^',quoting=csv.QUOTE_NONNUMERIC)
		csv_write.writeheader()
		for l in csv_read:
			del l['High']
			csv_write.writerow(l)

