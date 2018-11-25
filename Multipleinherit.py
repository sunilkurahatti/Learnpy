class father():
	def __init__(self):
		print("I Play foot ball")
	def cod(self):
		print("I am a good programer")

class mother():
	def sing(self):
		print("I sing")
	def cook(self):
		print("I cook good food")

class kid(father,mother):
	def cyc(self):
		print("Am an athelete")

ki=kid()
ki.cod()
ki.sing()
ki.cook()
ki.cyc()