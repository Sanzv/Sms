'''class Student():
	student_list=[]
	def __init__(self,num):
		for i in range(num):
			self.inputData()

	def inputData(self):
		name= input("Enter Students's name: \t")
		address=input("Enter Student's address: \n")
		self.student_list.append(name)

	def printData(self):
		for name in self.student_list:
			print("--> {} ".format(name))

num=int(input("Enter the number of students: \t"))
stu_1=Student(num)
stu_1.printData()'''

class Student():

	def __init__(self,name,address):
		self.name=name
		self.address=address

	def showStudent(self):
		print("Name --> {} \n Address --> {} ".format(self.name,self.address))

count=int(input("Enter the number of students: \t"))
student_list=[]
for i in range(count):
	name= input("Enter name of student {} : \t".format(i+1))
	address=input("Enter address of student {}: \t".format(i+1))
	student=Student(name,address)
	student_list.append(student)

for stu in student_list:
	stu.showStudent()

studentMap=map(lambda stud: stud.showStudent,student_list)
print(list(studentMap))