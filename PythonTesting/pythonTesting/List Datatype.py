#List DataType
#List datatype is a mutable datatype
# we can update the values
# use [] for creating list

z = [ 1, 1.2 , "Megha", 8, "Dhaduti"]
print(z[0])                      #1
print(z[3])                    #8
print(z[-1])                  # Dhaduti
print(z[1:4])                  # [1.2, 'Megha', 8]
z.insert(3, "kadesh")      # inserting
print(z)                                   #[1, 1.2, 'Megha', 'kadesh', 8, 'Dhaduti']
z.append("Chimmad")                        # appending
print(z)                                   #[1, 1.2, 'Megha', 'kadesh', 8, 'Dhaduti','Chimmad']
z[2]= "megha"                              # updating
print(z)                                     #[1, 1.2, 'megha', 'kadesh', 8, 'Dhaduti','Chimmad']
del z[4]                                    # deleting
print(z)                                    #[1, 1.2, 'megha', 'kadesh', 'Dhaduti','Chimmad']


# Tuple Datatype
# same as List datatype but it is immutable datatype
# use () for creating Tuple


v = (1,2,4,"megha", 8.9)
print(v[0])

#v[3] ="Megha"
#print(v)


# Dictionary datatype is "key:value"
# use {} for creating
#use "" value is string wheter it is in key or value position

m = {"a":"Megha", 2:"Dhaduti", 4:5, "kadesh":"Chimmad"}
print(m["a"])
print(m[2])
print(m["kadesh"])
print(m[4])


n = {}
n["megha"] = "kadesh"
n["a"] = 7
print(n)
print(n["a"])



