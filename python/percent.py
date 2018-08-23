# Calculating Percentage 

n=int(input("Enter number of subjects:  "))
sum=0.0
marks=0
for i in range(0,n):
    marks=int(input("Enter marks in subject {} :  ".format(i+1))) 
    if(marks<=100 and marks>=0):
    	sum = sum + marks
    else:
    	print("Enter Valid Marks.")
    	n++
    	
percentage=sum/n
print("Your percent is : {} %".format(percentage))
