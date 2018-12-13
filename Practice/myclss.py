import time

class Human():
	def __init__(self,n,o):
		self.name=n
		self.occupation=o

	def do_work(self):
		if self.occupation=="tennis":
			print(self.name,"Plays Tennis")
		elif self.occupation=="actor":
			print(self.name,"I shoot films")
	def speak(Human):
		print(Human.name,"Says Hi there have a good day")

sun=Human("Suni Kurahatti","actor")
sun.do_work()
sun.speak()

sush=Human("Sush Hanami", "tennis")
sush.do_work()
sush.speak()