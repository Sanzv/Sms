class person:
	name="Sanjeev"
	course="Python"

	def getName(self):
		return(self.name)
	def getCourse(self):
		return(self.course)

class ball:
	radius="6 inches"
	color="Red"

	def getRadius(self):
		return(self.radius)
	def getColor(self):
		return(self.color)

student= person()
print(student.getName())
print(student.getCourse())
sample= ball()
print(sample.getRadius())
print(sample.getColor())