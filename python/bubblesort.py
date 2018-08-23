list=[4,1,6,5,9]
for i in range (0,len(list)):
	for j in range(0,len(list)-i-1):
		if(list[j]> list[j+1]):
			temp=list[j]
			list[j]=list[j+1]
			list[j+1]=temp

print(list)