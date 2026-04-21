class Student:
    college = "Abc"
    #default constructor
    def __init__(self):
        pass
    #parameterised constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")
    def welcome(self):
        print("welcome student",self.marks)
    def get_marks(self):
        return self.get_marks
s1 = Student("Khushi",90)
print(s1.name,s1.marks)
print(Student.college)
s1.welcome()
print(s1.get_marks())