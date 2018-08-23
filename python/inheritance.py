class Employee():
	raise_amt=1.04

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.email=first + '.' + last +'@email.com'
		self.pay=pay

	def full_name(self):
		return '{} {}'.format(self.first,self.last)
	
	def apply_raise(self):b
		self.pay=int(self.pay * self.raise_amt)

class Developer(Employee):
	raise_amt=1.4
	
	def __init__(self, first,last,pay,prog_lang):
		 #Employee.__init__(self,first,last,pay)    Can be done like this
		 super().__init__(first,last,pay)
		 self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first,last,pay,employees=None):
		 #Employee.__init__(self,first,last,pay)    Can be done like this
		 super().__init__(first,last,pay)
		 
		 if employees is None:
		 	self.employees=[]
		 else:
		 	self.employees=employees

	def add_emps(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emps(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->',emp.full_name())




emp_1=Employee('Sushant','Khakurel',40000)
dev_1=Developer('Vijay','Dhakal',45000,'Android')
print(emp_1.email) #employee
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(dev_1.email)    #Developer
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)

mgr_1=Manager('Sanjeev','Roka','95000',[emp_1])
mgr_1.add_emps(dev_1)
mgr_1.remove_emps(emp_1)


mgr_1.print_emps()