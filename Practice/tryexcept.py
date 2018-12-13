
x=input("Enter First numner\n")
y=input("Enter Second number\n")

try:
	z=int(x)/int(y)
	print(z)
except ZeroDivisionError as a:
	z="Dummy"
	print("Exception occered", a)
except TypeError as e:
	print("I Dont Know",e)

finally:
	
	print("Have a good day pal")
	print(z)