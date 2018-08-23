def calcPrice(total,price):
	return(price+int(total))

machineList=[{
		'Snumber':1,
		'Item':'Television',
		'Price':32000
},
{
		'Snumber':2,
		'Item':'Fridge',
		'Price':12000
},
{
		'Snumber':3,
		'Item':'Fan',
		'Price':3500
},
{
		'Snumber':4,
		'Item':'Laptop',
		'Price':75000
}
]
print(machineList[0].keys(),end=' ')
print("\n")
for machine in machineList:
	print("{}\t{}\t{} ".format(machine['Snumber'],machine['Item'],machine['Price']))
	
total=0
choice='y'
list=[]
while (choice=='y'):
	orderNo=int(input("Enter the Serial Number of the Item:\t"))
	for item in machineList:
		if orderNo==item['Snumber']:
			total=calcPrice(total,item['Price'])
			list.append(item['Item'])
			
	choice=input("Do you want to Continue: (y/n)\t")
else:
	print("You ordered : {} ".format(list))
	print("Your total Amount becomes : {}".format(total))