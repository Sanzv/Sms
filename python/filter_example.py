directory = [{
	'name':'BroadWay infosys',
	'phoneNumber': '014356778',
	'location':'kathmandu'
},
{
	'name':'Kantipur Media',
	'phoneNumber': '014344557',
	'location':'kathmandu'
},
{
	'name':'Mero Bato',
	'phoneNumber': '014444478',
	'location':'kathmandu'
},
{
	'name':'Hamro Bato',
	'phoneNumber': '01555448',
	'location':'kathmandu'
}

]


found=False
conti='y'
while(conti=='y'):
	choice = input("Enter a company Name  : \t")
	result=list(filter(lambda x:x['name']==choice,directory))
	if not result:		            # we can check using length of the list
		found=False
		print("Enter Valid Name. \n")
	else:
		for j in result[0].keys():
			print(" {} -> {}\n ".format(j,result[0][j]))
		found=True
	conti=input("Want more Details ? \n (y/n) \n")
	
print("Thats All")
