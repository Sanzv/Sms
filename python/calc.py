#Making a simple calculator
print("\n\t\t CALCULATOR \n")
decide='y'
while(decide=='y'):
	result=0
	x=int(input("\tEnter First Number : "))
	y=int(input("\tEnter Second Number : "))
	operator= input('''\tWhat do you want to perform? 
\tAdd='+'
\tSubtract='-'
\tMultiply='*'
\tDivision='/'
''')
	if(operator=='+'):
		result=x+y
	elif(operator=='-'):
		result=x-y
	elif(operator=='*'):
		result=x*y
	elif(operator=='/'):
		if(y==0):
			result="\t Math Error  !!! "
		else:
			result=x/y
	else:
		print("\tEnter Valid operator.")
	print("\tThe result is \n {} {} {} = {}".format(x,operator,y,result))
	decide=input("\tDo you want to continue? \n Yes='y' \n No='n' \n")

else:
	prnit("\tThats all !!! ")