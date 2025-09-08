class Parent:
    def __init__(self,p1):
        print("I'm Parent constructor")
    def parent_method(self):
        return "I'm Parent"


class Parent2:
    def __init__(self,p2,p3):
        print("I'm Parent2 constructor")
    def parent2_method(self):
        return "I'm Parent2"


class Child1(Parent2,Parent):
    def __init__(self,p2,p3):
        super().__init__(p2,p3)
        # super().__init__()
        print("I'm Child1 constructor")
    def child1_method(self):
        return "I'm Child1"



c1 =Child1("Hi","Hello")



