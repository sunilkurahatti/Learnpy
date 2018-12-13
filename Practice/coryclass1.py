class Employee():
	amt_raise = 1.20
	
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
	@classmethod
	def set_raiseamt(cls,raise_amt):
		cls.amt_raise=raise_amt

	@classmethod
	def parse_emp(cls,new_str):
		# cls.new_str=new_str
		first,last, pay = new_str.split('-')
		return cls(first,last, pay)
	@staticmethod
	def isworkday(w_date):
		if w_date.weekday() == 5 or w_date.weekday()==6:
			return False
		return True


emp_1=Employee(pay=40000,first="Sunil",last="Kurahatti")

emp_2=Employee("test","user",60000)

# print(emp_1.email,emp_1.pay)
# print(Employee.fullname(emp_2))
# # print(emp_1.fullname())
# print("New salary after raise is :",Employee.pay_raise(emp_2))
# print(emp_2.amt_raise)
# print(Employee.amt_raise)
emp_1.set_raiseamt(1.7)
# emp_2.amt_raise=1.1
Employee.amt_raise

# print("New salary after raise is :",Employee.pay_raise(emp_2))
# print(Employee.set_raiseamt(1.5))
print(emp_1.amt_raise)
print(emp_2.amt_raise)

new_emp1_1='Anil-kurahatti-70000'
new_emp12_2='tom-jerry-20000'
new_ert=Employee.parse_emp(new_emp1_1)

# # Employee.parse_emp(new_emp1_1)
# # print(Employee.parse_emp(new_er))
# # print(new_er.first)
print(new_ert.first)
print(new_ert.pay)
print(Employee.fullname(new_ert))

import datetime

in_day=datetime.date(2004,4,12)
print(Employee.isworkday(in_day))