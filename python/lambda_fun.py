prod = lambda x,y : print(x*y)
div = lambda x,y : x/y
x=int(input("Enter First Value:\t"))
y=int(input("Enter Second Value:\t"))
print(prod(x,y))
print(div(x,y))
print(type(prod))
prod= map(lambda x :x**2,[0,1,2,3,4])
print(list(prod))

data = [{'name':'yubaraj', 'address':'itahari', 'course':'python'},
		{'name':'hari', 'address':'kathmandu', 'course':'android'},
		{'name':'shyam', 'address':'pokhara', 'course':'java'},
		{'name':'raju', 'address':'pokhara', 'course':'python'}]
allName=[]
allName.append(list(map(lambda x:x['name'], data)))
allName.append(list(map(lambda x:x['address'], data)))
allName.append(list(map(lambda x:x['course'], data)))
for name in allName:
	print(name)
for i in range(len(allName)):
	print(allName[i])

print(allName)