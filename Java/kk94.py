class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum = 0
            sum += val
        print("hello",self.name,sum/3)
s1 = student("Khushi",[7,7,7])
s1.get_avg()