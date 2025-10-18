class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")


class Employee(Person):
    def __init__(self,name,age,BU,Team):
        super().__init__(name,age)
        self.BU=BU
        self.Team=Team
    def display_infomain(self):
        Person.display_info(self)
        print(f"BU is {self.BU}")
        print(f"Team is {self.Team}")

d=Employee("Sai Kumar",26,"BRCC","Output Services")
d.display_infomain()