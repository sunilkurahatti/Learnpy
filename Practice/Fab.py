#Fabonacci Series

def fab(n):
	a,b=0,1
	while a<n:
		print(a)
		a,b=b,a+b
	print(a)


def fab1(n):
	result=[]
	a,b=0,1
	while a<n:
		result.append(a)
		a,b=b,a+b
	return result
	
# if __name__=="__main__":
# 	import sys
# 	fab(int(sys.argv[1]))

	