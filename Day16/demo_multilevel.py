class Parent:
    def parent_method(self):
        return "I'm Parent"


class Child(Parent):
    def child_method(self):
        return "I'm Child"


class GrandChild(Child):
    def grand_child_method(self):
        return "I'm grand Child"


p = Parent()
c= Child()
gc=GrandChild()

# p.parent_method()
# c.parent_method()
# gc.grand_child_method()