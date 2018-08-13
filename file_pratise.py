'''with open("file.txt",'r+',encoding='utf-8') as f:
	print(f.readline(),end='***')
	print(f.readline(),end='***')
	print(f.read(20),end='***')
	print(f.read(),end='***')
	f.seek(50)
	print(f.read())

with open("anup.png",'rb') as fr:
	with open("anup_copy.png",'wb') as fw:
		len_to_read = 10
		fr_contents=fr.read(len_to_read)
		while len(fr_contents)>0:
			fw.write(fr_contents)
			fr_contents=fr.read(len_to_read)'''
print("\n\t\t***********BROADWAYS STUDENTS MIS************\n")
cont='y'
while(cont=='y'):
	choice=int(input("\t\t1. Enter Records \n\t\t2. Read Records\n\n\t\t"))
	if choice==1:
		name=input("Enter students name : \t")
		address=input("Enter students address: \t")
		option=input("\tDo you want to save the record? \n Save(y/n)\t")
		if option=='y':
			with open("studentsRecords.txt",'a+') as f:
				f.write("Name : " + name + "\t")
				f.write("Address : " + address + "\n")
				print("\nData save successfully.")
		elif option=='n':
			print("\nRecord not saved.")
			print("\nYou entered : \n Name:\t {} \t address:\t {}\n".format(name,address))
			exit()
		else:
			print("\nEnter valid option.")
	elif choice==2:
		try:
			with open("studentsRecords.txt",'r') as f:
				print(f.read())
		except:
			print("\n\n\t\tNo records were saved.")
	else:
		print("\n\n\t\tEnter Valid Choice.")

	cont=input("\n\n\tDo you want to continue? \t (y/n)\t\t")   #Reading value for continuing

else:
	print("Thats all.")                #Else for the while Loop