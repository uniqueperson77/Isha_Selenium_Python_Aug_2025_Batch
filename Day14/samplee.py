s= "Isha"
s.split()

emp1_name = "Virat"
emp2_name = "Sehwag"
emp3_name = "Sachin"
emp1_surname = ""
emp1_age = 30
emp1_gender= ""

#normal class
class Employee:
    # name = ""
    # age = ""
    # surname = ""
    # salary = ""

    def __init__(self,name,salary,surname=None,height=None,age=None):
        self.name = name
        self.salary = salary
        print("This method has been called implicitly")

    def __str__(self):
        return "This is a dunder method and having value of " + self.name


    def speak(self,times):
        print("speaking")


    def walk(self):
        print(self.salary,self.name)

    def play(self):
        pass


isha = Employee("Isha",5000)
zaheer = Employee("Zaheer",10000)

print(zaheer)
print(isha)

# print(isha.salary)
# print(zaheer.salary)

# print(emp1.salary)
# emp1.speak()

# zaheer.walk()


