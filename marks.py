class Marks:
	sub_list=[] 

	def __init__(self,subject,mark):
		for i in range(len(subject)):
			sub={'sub_name':subject[i], 'marks':mark[i]}
			self.sub_list.append(sub)
		print("Your percentage is : {} \n".format(self.calcPercentage()))
		self.findDivision()

	def calcPercentage(self):
		total=0
		for subject in self.sub_list:
			total= total + subject['marks']
		self.percent=total/len(self.sub_list)
		return self.percent

	def getSubjects(self):
		for members in self.sub_list:
			print("{}  -->  {}".format(members['sub_name'],members['marks']))
	
	def findDivision(self):
		if (self.percent >= 80 and self.percent <=100):
			print("Distinction")
		elif (self.percent >=60  and self.percent < 80):
			print("First Division")
		if (self.percent >=40 and self.percent < 60):
			print("Second Division")
		else:
			print("Winner !!!")
subjects=[]
marks=[]
count=int(input("Enter number of subjects. \t"))
for i in range(count):
	sub_name=input("Enter name of subject : \t")
	mark=int(input("Enter marks : \t"))
	subjects.append(sub_name)
	marks.append(mark)
mark1=Marks(subjects,marks)
mark1.getSubjects()
