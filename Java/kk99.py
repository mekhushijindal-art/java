class student:
    def ___init__(self,name):
        self.name = name
        
s1 = student("Khushi")
print(s1.name)
del s1.name
print(s1.name)