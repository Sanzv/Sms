initial="---------\n|\t |\n|\n|\n|\n|\n|\n|\n|\n--------"
firstw="---------\n|\t |\n|\t O\n|\n|\n|\n|\n|\n|\n--------"
secondw="---------\n|\t |\n|\t O\n|\t/|\\\n|\n|\n|\n|\n|\n--------"
thirdw="---------\n|\t |\n|\t O\n|\t/|\\\n|\t |\n|\n|\n|\n|\n--------"
fourthw="---------\n|\t |\n|\t O\n|\t/|\\\n|\t |\n|\t/|\\\n|\n|\n|\n--------"
#fifthw="---------\n|\t|\n|\tO\n|\t|\n|\t/\n|\t\\n|\t|\n|\n|\n--------"
#sixthw="---------\n|\t|\n|\tO\n|\t|\n|\t/\n|\t\\n|\t|\n|\t/\n|\n--------"
#seventhw="---------\n|\t|\n|\tO\n|\t|\n|\t/\n|\t\\n|\t|\n|\t/\n|\t\\n--------"
pics=[firstw,secondw,thirdw,fourthw]
questions={
	'What\'s the full form of URI?':'universal resource indicator',
	'What is the height of sagarmatha in meters?':'8848',
	'What is the capital of Poland?':'warsaw',
	'Who is the GOAT? Give full name.':'lionel messi',
	'Who won the FIFA World Cup 2018?':'france',
	'National Animal of Nepal?':'cow',
	'Number of sense organs?':'5'
}
score=0
wrong=0
correct=0
print(initial)
for item in questions.keys():
	print("\tYou have answered {} Questions correctly.".format(correct))
	print("\tYour Score is : {}".format(score))
	print("\n\tYour Question is : \n\t {}".format(item))
	ans=input("\tEnter your answer: \n \t\t")
	ans=ans.lower()
	if ans == questions[item]:
		print("\tCorrect answer.\n")
		score+=5
		correct+=1
		if correct==len(questions)-1:
			print("\t********Shit Head. !!!!! You Won the game***********")
	else:
		print("\tWrong answer")
		print("\tCorrect Answer is : {}".format(questions[item]))
		print("{}".format(pics[wrong]))
		wrong+=1
		if wrong < len(questions):
			continue
		else:
			print("******** GAME OVER *********\n **********LOSER***********")