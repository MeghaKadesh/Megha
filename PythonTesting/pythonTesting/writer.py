#  Qn --- write all contant in text file in reverse
#read file and store all lines in the list
#reverse the list
#write list back to the file

with open('test.txt','r') as reader: #[mkul, nju,fdsk, gyhh,juioo]
    con = reader.readlines()         #[juioo, gyhh, fdsk,nju,mkul]
    reversed(con)
    with open('test.txt','w') as writer:
        for i in reversed(con):
            writer.write(i)

