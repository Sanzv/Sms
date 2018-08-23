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

print(directory[1])
for i in range (len(directory)):
	print(directory[i])
	for j in directory[i].keys():
		print("{key} has {values}".format(key=j, values=directory[i][j]))
found=False
name=input("Enter Company name : \t")
for company in directory:
	if name==company['name']:
		print("Phone Number = {} \n location= {} ".format(company['phoneNumber'],company['location']))
		found=True
		break
if(found==False):
	print("Invalid Company Name.\n")