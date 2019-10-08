#Here is source code of the Python Program to Calculate the Average of Numbers in a Given List. 
#The program output is also shown below.

n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))
