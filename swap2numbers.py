#Here is source code of the Python Program to exchange
#the values of two numbers without using a temporary variable.
#The program output is also shown below.

a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a," b is:",b)
