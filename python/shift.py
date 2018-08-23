#shifting elements in lists
n=int(input("Enter number of elements: \n"))
list=[]
list1=[]
i=0
print("Enter numbers:\n")
while i!=n:
	var= int(input("\t"))
	list.append(var)
	list1.append(var)
	i=i+1
print("Your list is\n {}".format(list))
'''for s in range(-(n),0): #Printing using negative index
	var=list[s]
	print(var)'''
shift=int(input("How many units to shift? \t"))
l=len(list)
temp1=0
for i in range(0,n):
	if(i+shift < n):
		list1[i+shift]=list[i]
	else:
		for j in range(0,shift):
				var=list[k]
				list1[j]=var
				k=k+1
		break
	stop=i
	k=stop+1


list=list1			
print("Shifted list is\n {}".format(list))