file_read = open('abc.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('abc.txt', 'w')
file_write.write(" File in write mode ....")
file_write.write("Hi! This is Ramisha.. ")
file_write.close()

file_append = open('abc.txt', 'a')
file_append.write("\n File in append mode ....")
file_append.write("Hi! This is Ramisha..")
file_append.close()