with open('abc.txt', 'w') as file:
  file.write("Hi! I am Ramisha.")
file.close()

with open('abc.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are..")
  for line in data:
    word = line.split()
    print (word)
file.close()