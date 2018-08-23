#Program to calculate Tax,VAT,Service Charge for a menu bill in the resturant
'''def calcTea(n,q):
	return(n*q)
	pass
def calcMomo(n,q):
	return(n*q)
	pass
def calcChowmein(n,q):
	return(n*q)
	pass
def calcFry(n,q):
	return(n*q)
	pass
def calcBurger(n,q):
	return(n*q)
	pass'''
def calcBill(total,vat,service_per):
	vatAmount=(vat/100)*total
	service_charge=(service_per/100)*total
	print("Vat Amount = {}".format(vatAmount))
	print("Service Charge = {}".format(service_charge))
	return(total+vat+service_charge)
	pass


print("\t******** MENU ********")
print('''
S.No		Item		Price
1		Tea		30
2		Mo:Mo		100
3		Chowmein	120 
4		Fry-Rice	90
5		Burger		120
''')
total=0
choice='y'
itemList=[]
quantList=[]
vat=13
service_charge=10
while choice=='y':
	orderNumber=int(input("Enter the S.No of the item : \t"))
	quantity = int(input("Enter the quantity: \t"))
	quantList.append(quantity)
	if(orderNumber==1):
		 price= 30* quantity		 	    #calcTea(30,quantity)
		 itemList.append("tea")
	elif(orderNumber==2):
		price=100*quantity 			 	    #calcMomo(100,quantity)
		itemList.append("Mo:Mo")
	elif(orderNumber==3):
		price=120*quantity					#calcChowmein(120,quantity)
		itemList.append("Chowmein")
	elif(orderNumber==4):
		price=90*quantity 					#calcFry(90,quantity)
		itemList.append("Fry-rice")								 
	elif(orderNumber==5):
		price=120*quantity 					#calcFry(120,quantity)
		itemList.append("Burger")			 
	else:
		 print("Enter Valid S.No.\n")

	total=total+price
	print("More Orders ??? ")
	choice=input(" Press 'y' to continue \n Press any other key ko get the amount \t")
else:
	i=0
	print("You ordered : \n")
	for var in itemList:
		print(var + "\t \t ",quantList[i])
		i=i+1
		print("\n")
	billAmount=calcBill(total,vat,service_charge)


print("Your Bill Amounts : %d" % (billAmount))