def add(x,y=6):
	"""
	Calculating the sum 
	this can have default arguement but here we are not using any
	"""
	return(x+y)

print("Enter Numbers to be added : \t")
x=int(input("\t"))
y=int(input("\t"))
print(add(x))
print(add.__doc__)