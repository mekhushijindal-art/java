class Person:
    name = "anonymous"
    @classmethod
    def ChangeName(cls, name):
        cls.name = name
p1 = Person()
p1.ChangeName("rahul kumar")
print(p1.name)
print(Person.name)