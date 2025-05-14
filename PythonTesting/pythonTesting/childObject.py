from Object_O_P_S import megha, megha1


class dha(megha):
    num2 = 70

    def __init__(self):
        megha.__init__(self, 4,2)

    def hk(self):
        return self.num2 + self.num + self.getdata()

oj = dha()
print(oj.hk())

class hug(megha1):

    def __init__(self):
        megha1.__init__(self, 9,1)

    def nn(self):
        return self.getdata1()

oj1 = hug()
print(oj1.nn())

