new_file = open('File.txt', 'x')
new_file.close()

import os
print("Checking if my_file exists or not!")
if os.path.exists("Newfile.txt"):
  os.remove("Newfile.txt")
else:
  print("The file does not exist")

my_file = open("Newfile.txt", "w")
my_file.write("Hi! I am Ramishaaa")
my_file.close()

os.remove('abc.txt')
os.rmdir('Folder')