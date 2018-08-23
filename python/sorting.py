#Sorting
n=int(input("Enter number of elements: \n"))
list=[]
list1=[]
i=0
print("Enter numbers to be sorted:\n")
while i!=n:
	var= int(input("\t"))
	list.append(var)
	i=i+1
print("Unsorted list is \n {} ".format(list))

l=len(list)
j=0
while j!=l:
	var1=min(list)
	list.remove(var1)
	list1.append(var1)
	j=j+1
list=list1
print("Sorted list is \n {} ".format(list))
