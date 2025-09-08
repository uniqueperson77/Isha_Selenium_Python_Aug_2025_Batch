# print(len("Hello World"))
# print(len([2,4,6,8,10]))


# print(1+1)
# print("1"+"1")


### based on the object, it will call or behave in that way
class Stringg:
    def move(self,p1,p2):
        print("string")

class Listt(Stringg):
    def move(self,p3,p4):
        super().move(p3,p4)
        print("list")


class Tuple:
    def move(self):
        print("tuple")


# Boat.move(Boat)

obj = Listt()
obj.move(1,1)

# obj1 = Stringg()
# obj1.move(1,1)

