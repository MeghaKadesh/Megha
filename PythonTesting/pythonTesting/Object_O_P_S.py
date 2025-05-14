# self keyword is mandetory for calling the variable name ito method
#instance and class variables have whole different perpose
#Constructor __init__ keyword



class cal:

    def ge(self):
        print("Megha")

obj = cal()
obj.ge()


class megha:
    num = 100

    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b

    def getdata(self):
        return self.firstnumber + self.secondnumber + megha.num
        


obj = megha(2, 3)
print(obj.getdata())



class kad:
    k = 900

    def __init__(self,c,d):
        self.a = c
        self.b = d
    def h(self):
        return self.a * self.b * self.k

n = kad(67,90)
print(n.h())



class meg:
    def __init__(self,v,l):
        self.first = v
        self.second = l
    def get(self):
        return self.first - self.second

ob = meg(4,7)
print(ob.get())


class megha1():

    def __init__(self,y,u):
        self.first = y
        self.second = u


    def getdata1(self):
        return self.first + self.second


obj1 = megha1(1,1)
print(obj1.getdata1())





