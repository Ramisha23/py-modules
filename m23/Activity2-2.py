file1 = open('abc.txt','r')
file2 = open('newabc.txt','w')

for line in file1.readlines():
	if not (line.startswith('hello')):	
		print(line)
		file2.write(line)

file2.close()
file1.close()