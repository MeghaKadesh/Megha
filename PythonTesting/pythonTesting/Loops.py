# if condition

a = "Good Morning"

if a == "Morning":
    print("Condition satisfy")
else:
    print("Condition false")
print("if condition is completed")

b= 2
if b<5:
    print("Condition true")
else:
    print("Condition false")



#for loop
abc = [1,2,3,4,5]
for i in abc:
    print(i)
print("******************")

# multiple of 2 for above loop

c = [1, 2, 3, 4, 5]
for i in c:
    print(i*2)
print("******************************")


# sum of 1st 5 natural numbers
summation = 0
for i in range(1,6):
    summation = summation+i
print(summation)
print("************")
#How to increment i+2

for j in range(1,7,2):
    print(j)
print("**************")

for k in range(3):
    print(k)
print("************")


#while loop
g = 6
while g>1:
    print(g)
    g = g-1

print("************")
d = 6
while d>1:
    if d!=3:
        print(d)
    d= d-1
print("********")

q = 6
while q>1:
    if q==3:
        break
    print(q)

    q=q-1

print("********")

w = 10
while w>1:
    if w==9:
        w=w-1
        continue
    if w==3:
        break
    print(w)
    w = w-1


