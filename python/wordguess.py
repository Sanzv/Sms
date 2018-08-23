import os
import json
with open("word.json",'r') as f:
	words=json.loads(f.read())


i=0
guessed=[]
for items in words.keys():
	correct=2
	print("You have \n \t\t {}".format(items))
	choice=input("Do you want to continue with this word? (y/n): \t").lower() 
	if choice=='y':
		while correct > 0:
			guess=input("Enter your guess: \t")
			guess=guess.lower()
			predictedIndex=[]
			if guess in words[items]:
				correct -= 1
				index = words[items].index(guess)
				if index in predictedIndex:
					print("Already Predicted")
				else:
					predictedIndex.append(index)
					print("Guess Other Letter.")
			else:
				print("Try Again")
		#if correct == 0:
			#print("YOur answer is : {}".format(list[i]))
			#i+=1
		else:
			input("Press any key to Proceed")
			os.system('cls')

	else:
		continue
else:
	print("That is all we have.")

		