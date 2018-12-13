class accident(Exception):
	def __init__(self,msg):
		self.msg=msg
	def print_exception(self):
		print("User defined Exception :",self.msg)

try:
	raise accident("Car crash happened")
except accident as e:
	e.print_exception()
