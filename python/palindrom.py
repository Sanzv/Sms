#finding whether given number is palindrome or not
number = int(input("Enter the number: "))
original = number
rev = 0
while(number > 10):
	rev = rev*10 + number%10
	number = number//10
else:
	rev = rev*10+number
	print(rev)
print("number = {givenNum} and reveresed number = {calculated}".format(givenNum=original, calculated=rev))
if original == rev:
	print("\n %s is palindrom number"%(original))
else:
	print("\nThis is not palindrome")