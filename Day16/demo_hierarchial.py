class Parent:
    def parent_method(self):
        return "I'm Parent"


class Child1(Parent):
    def child1_method(self):
        return "I'm Child1"

class Child2(Parent):
    def child2_method(self):
        return "I'm Child2"


class Child3(Parent):
    def child3_method(self):
        return "I'm Child2"


# c2 = Child1()
# c2.