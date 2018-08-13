class Books:
	def __init__(self,ids,name,author,edition):
		self.ids=ids
		self.name=name
		self.author=author
		self.edition=edition

	def getName(self):
		return self.name

	def getAuthor(self):
		return self.author

	def getEdition(self):
		return self.edition

	def __str__(self):
		return self.name

	#def assignBookToStudent(self,student):

book1=Books(1,"Think and Grow Rich","Aalu",2018)
print(book1.getName(),book1.getAuthor(),book1.getEdition())
print(book1.__str__())