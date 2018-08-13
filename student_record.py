from book import Books
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
with open("studentsrecord.txt",'a+',encoding='utf-8') as f:
	for item in student_list:
		f.write(str(item))

for stu in student_list:
	stu.showStudent()

book1=Books(2,"Learning Python","Anoconda",2018)
print(book1.getName() , book1.getAuthor())
student_name=input("Enter name of student to assign book:\t")