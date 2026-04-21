marks = int(input("Enter student marks"))
if(marks>90):
       grade = "a"
elif(marks>=80 and marks<90):
       grade =  "b"
elif(marks>=70 and marks<80):
       grade =  "c"
else:
       grade  = "d"
print("Grade of the student", grade)