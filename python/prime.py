#finding prime numbers between 1 and 100
#flag=1
num=int(input("Enter a Number:  "))
'''for i in range(2,num//2):
	if(num%i == 0):
		flag=0
		break
if(flag==0):
	print("{} is a composite number. \n".format(num))
else:
	print("{} is a Prime number. \n".format(num))'''

#Printing prime numbers between 1 and 100
'''print("\n \t Prime Numbers upto {} are : \n \t".format(num))
for i in range(2,num+1):
	flag=1
	for j in range(1,i//2+1):
		if(i%(j+1) == 0):
			flag=0
			break
	if(flag==1):
		print(i,end=',')
	elif(i==2):
		print(i,end=',')'''

for i in range(3, 100):
	for j in range (2, i):
		if(i % j == 0):
			break
		
	if(i == j+1):
		print("%s is prime number"%(i))	 


	
