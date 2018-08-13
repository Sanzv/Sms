with open("file1.txt",'r+',encoding='utf-8') as f:
	f.write("This line will append\n")
	f.write("This line will append too \n\n")
	f.write("Final Line")
	print(f.read())

with open("file.txt",'r',encoding='utf-8') as fr:
	print(fr.tell())
	read_size_of=10
	f_contents=fr.read(read_size_of)
	while(len(f_contents) > 0):
		print(f_contents,end='')
		f_contents=fr.read(read_size_of)
	print(fr.tell())
