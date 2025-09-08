class Sport:
    #class variables
    a="Cricket"
    b="Football"

    def __init__(self,p1,p2):     #constructor
        self.var1 = p1     #instance variable
        self.var2 = p2      #instance variable

    def method1(self):
        pass

    def method2(self,p1):
        pass


# inst = Sport()
# #ways of accessing class level variables
# print(inst.b)
# print(Sport().a)

obj1 = Sport("Hockey","Kabadi")
obj2 = Sport("Throw ball","Game2")
print(obj1.var1)
print(obj2.var1)
print(obj1.b, obj2.b)
obj1.method1()
obj2.method2("abcd")




