class parent():
	def f1(self):
		print("this is parent class")

class child(parent):
	def f2(self):
		print("this is child class")

cl=child()
cl.f2()
cl.f1()