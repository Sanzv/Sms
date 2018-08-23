import json
import os
import time
import random
with open("questions.json",'r') as f:
	questions=json.loads(f.read())
global point
global correct
def start():
	point=0
	correct=0
	'''arr=[a1,a2,a3]
	randomIndex = random.randint(0,2)
	nextQuestion = question[arr[randomIndex]]'''
	for question in questions:
		print("Your Current Point is: {}".format(point))
		print(question['q'])
		print("Your Options are: \n")
		print("a)" , question['a'] , "\t" ,"b)" ,question['b'])
		print("c)" , question['c'] , "\t" ,"d)" ,question['d'])
		ans=input("\tEnter the answer. \t(a / b / c / d) \t")
		'''choice=helpLine()
		if choice=='a':
				print("Your Options are: \n")
				compulsary=question['ca']
				print("a)" , question['question['ca']'] , "\t" ,"b)" ,question['b'])'''
		if ans==question['ca']:
			print("*******Correct Answer.**********")
			point+=10
			print("\tYour Point becomes  {}".format(point))
			correct+=1
		else:
			print("Opps.. You got it Wrong.  Try another.")
			print("Correct answer is {}".format(question['ca']))
			print("\tYour Point is still {}".format(point))
		time.sleep(5)
		os.system('cls')
	else:
		print("Total Right answers : {}".format(correct))
		print("Total Points : {}".format(point))

def helpLine():
	print("You have following options.")
	choice=input("a) 50/50  \t b) Audience Poll \n Any other key to Not take helpline. ")
	return(choice)

start()
