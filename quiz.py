import json
import os
import time
import random
with open("questions.json",'r') as f:
	questions=json.loads(f.read())
global point
global correct

def hp():
	print("You have following options.")
	choice=input("a) 50/50  \t b) Audience Poll \n Any other key to Not take helpline. \n\t")
	return choice

point=0
correct=0
'''arr=[a1,a2,a3]
randomIndex = random.randint(0,2)
nextQuestion = question[arr[randomIndex]]'''
print("********Welcome to the Game********")
name=input("Enter Your Name: \t ")

for question in questions:
	print("Your Current Point is: {}".format(point))
	print(question['q'])
	print("Your Options are: \n")
	print("a)" , question['a'] , "\t" ,"b)" ,question['b'])
	print("c)" , question['c'] , "\t" ,"d)" ,question['d'])		
	helpline=input(("Do you want to take the helpline? (y/n) \t"))
	if helpline=='y':
		choice=hp()
		if choice=='a':
			list=['a','b','c','d']
			print("Your Options are: \n")
			compulsary=question['ca']
			list.remove(compulsary)
			alt=random.choice(list)
			print("Your New Options Are: ")
			print(compulsary ,")",question[compulsary] , "\t" ,alt,")" ,question[alt])

	ans=input("\tEnter the answer. \t(a / b / c / d) \t")

	if ans==question['ca']:
		print("*******Correct Answer.**********")
		point+=10
		print("\tYour Point becomes  {}".format(point))
		correct+=1
	else:
		print("Opps.. You got it Wrong.  Try another.")
		print("Correct answer is {}".format(question['ca']))
		print("\tYour Point is still {}".format(point))
	time.sleep(1)
	os.system('cls')
else:
	with open("details.txt",'a+') as f:
		f.write(name)
		f.write(correct)
		f.write(point)
	print("Total Right answers : {}".format(correct))
	print("Total Points : {}".format(point))
