'''student = {'name': 'hari', 'surname': 'pandey'}
print(student['name']) #Gives Initialized Value
student['name'] = 'shyam'  # set the value
print (student['name']) # print the value.
student['roll'] = 34 # Add a new key 'roll' with the associated value
print (student.keys()) # print out a list of keys in the dictionary
print ('roll' in student) # test to see if 'roll' is in the dictionary.  This returns true.
sample_dist={}
sample_dist={'python':['Sanjeev','Aalu'],'course':'python','studentsFrom':['kathmandu','bhaktapur']}
for dict_key in sample_dist.keys():
	print(dict_key)
	print("{key} has {values}".format(key=dict_key, values=sample_dist[dict_key]))
'''
directory={'companyName':['x','y','z'],'companyNumber':[123,456,789],'companyLoc':['A','B','C']}
name=input("Enter Company's name :  \t")

for details in directory.keys():
	print(" {key} -> {values} ".format(key=details,values=directory[details]))
i=0
for search in directory['companyName']:
	if(search==name):
		number=directory["companyNumber"][i]
		location=directory["companyLoc"][i]
		break
	i=i+1

print(number,location)