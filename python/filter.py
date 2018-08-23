data = [{'name':'yubaraj', 'address':'itahari', 'course':'python'},
		{'name':'hari', 'address':'kathmandu', 'course':'android'},
		{'name':'shyam', 'address':'pokhara', 'course':'java'},
		{'name':'raju', 'address':'pokhara', 'course':'python'}]

allName = list(filter(lambda x:x['address']=='pokhara' AND x['course']=='java', data))
fewName = list(filter(lambda x:x['address']!='pokhara', data))
print(allName)

print(fewName)