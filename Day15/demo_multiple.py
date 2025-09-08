class Parent1:
    p1=""
    def __init__(self,*args):
        self.pa1 = args[0]
        self.pa2 = args[1]
    def method1(self):
        pass


class Parent2:
    p2=""
    def __init__(self,p):
        self.par1 = p

    def method2(self):
        pass

class Parent3:
    p2=""
    def __init__(self,p3,p4):
        self.par1 = p3
        self.par2 = p4

    def method2(self):
        pass


class Child(Parent1,Parent3,Parent2):
    # pass
    def __init__(self,*args):
        super().__init__(*args)


print(Child.p1)
obj = Child(1,2)
obj.method2()
obj.method1()