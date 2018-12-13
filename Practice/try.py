while True:
	try:
		x=int(input("please enter a number\n"))
		break
	except ValueError:
		print("oops not a integer")
	except:
		print("idont know what it is")
		# raise
