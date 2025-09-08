class Parent:
    a=""
    b=""
    def method1(self):
        print("This method1 belongs to Parent class")


class Child(Parent):
    def method2(self):
        print("This method2 belongs to Child class")


ch =Child()
ch.method1()
ch.method2()

par = Parent()
par.method2()

