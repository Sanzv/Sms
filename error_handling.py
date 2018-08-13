
try:
	marks=input("Enter the marks:\t")
	percent=marks/10
	print(marks)
	raise ZeroDivisionError

except:
	print("String cannot be divided by integer. Correct the Code.\n")

#else:
	#  If no error and doesnt enter except this section runs
	
#finally:
	#  Runs anyways