#find the gratest of 3 number entered by the user
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if(a >= b and a >= c):
    print("First number is largest",a)
elif(b >= c):
    print("second number is largest",b)
else:
    print("third number is largest",c)