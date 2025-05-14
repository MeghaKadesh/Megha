file = open('test.txt')
#or
#with open('test.txt','r') as reader:
#print(file.read())
#read all the content of the file
#read n number of characters by passing parameters
#read single line at a time
#read line by line using readline method

#print(file.readline())
#print(file.readline(4))



#if we have more lines how to print

#using while or for loops


#line = file.readline()
#while line!="":
 #   print(line)
 #   line = file.readline()
#file.close()


#using for loop

for i in file.readlines():
    print(i)



