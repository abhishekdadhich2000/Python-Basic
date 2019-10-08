#Here is the source code of the Python Program to read a number n and compute n+nn+nnn.
#The program output is also shown below.

n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)
