# Drawing pattern
n=int(input("How many lines do you want to print? \n"))
i=1
j=0
for i in range(n+1):
	for j in range(i):
		print("*",end="")
	print("/n")
	

