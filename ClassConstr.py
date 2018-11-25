class sunil:

	b=45
	l=['Sunil','Anil','Sush','Santosh']
	dt={1:'sunil',2:'Kurahatti'}

	def __init__(self):
		print("Myname is sunil",self.l)
		print(self.l[2])
		print(self.l)
		print(self.dt[2])

	def add(self,a):
		x=a+self.b
		print(x)

sn=sunil()
sn.add(34)
