class Employee():
	amt_raise = 1.10
	
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=self.first+'.'+self.last+'@gmail.com'

	def fullname(self):
		return '{},{}'.format(self.first,self.last)

	def pay_raise(self):
		new_pay=int(self.pay*self.amt_raise)
		return new_pay

class developer(Employee):
	amt_raise = 1.50
	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang=prog_lang

class Manager(Employee):
	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees=[]
		else:
			self.employees=employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print("---->", emp.fullname())


emp_1=developer(pay=40000,first="Sunil",last="Kurahatti", prog_lang='Python,Cython')

emp_2=Employee("test","user",60000)

# man_1=Manager(pay=40000,first="manfn",last="manln",employees=[emp_1])

man_1=Manager('Anil','Kurahatti', 50000,[emp_2])

# emp_2=Employee("test","user",60000)
# print(emp_1.email)
# print(emp_1.prog_lang)`
# print(emp_2.prog_lang)

# print(Employee.pay_raise(emp_1))
# print(emp_2.pay)
# print(Employee.pay_raise(emp_2))
# man_1.add_emp(man_1)
man_1.add_emp(emp_1)
print(Manager.print_emp(man_1))

print("-------------------------------------")

# man_1.remove_emp(emp_1)
man_1.remove_emp(emp_2)
print(Manager.print_emp(man_1))