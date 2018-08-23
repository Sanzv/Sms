'''import json 
with open("sample.json",'r') as sampleJSON:
	#print(sampleJSON.read())
	jsonData = json.loads(sampleJSON.read())
	print(jsonData)

	for data in jsonData:
		print(type(data)) '''

import requests
import json
url="http://github.yubrajpoudel.com.np/others/sample1.json"
data =requests.get(url)
print(data.text)
jsonData =json.loads(data.text)

for person in jsonData:
	print("Name is {name} and email is {email} ".format(name=person['name'],email=person['email']))