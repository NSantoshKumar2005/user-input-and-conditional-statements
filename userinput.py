'''User input
--------------
int data type
----------------
Ex:'''
any=int(input("Enter a number:"))
print(type(any))
'''
passing two values
-------------------------
Ex:'''
a,b=map(int,input("Enter two numbers: ").split())
print(a)
print(type(a))
print(b)
print(type(b))
'''
string data type
--------------------
Ex:'''
an=input("Enter the word: ")
print(type(an))
'''
List data type
-----------------
Ex:'''
cv=list(map(int,input("Enter the number: ").split()))
print(type(cv))
print(cv)
'''
Tuple data type
--------------------
Ex:'''
AM=tuple(map(int,input("Enter the numbers:").split()))
print(type(AM))
print(AM)
'''
f-string
---------
Ex:'''
A=11
B=2
print("{A}+{B} =",A+B)
print(f"{A}+{B} ={A+B}")
'''
if statement
---------------
This is used to check condition is true or not
Ex:
'''
an=1
if an>=2:
    print(f"{an} is greater than equal to 2")
else:
    print(f"{an} is less than equal to 2")

'''
else statement
--------------------
-->else is a fall-back statement, incase if statement becomes false,it will enter into else
Ex:'''
an=2
if an>=3:
    print(f"{an} is greater than equal to 3")
else:
    print(f"{an} is less than equal to 3")
'''
write a program to check whether the given number is greater or lesser'''
an,b=map(int,input("Enter the values:").split())
if an>b:
    print(f"{an} is greater than equal to {b}")
else:
    print(f"{an} is not greater than {b}")
'''
write a program to check whether the person is eligible to vote are not'''
age=int(input("Enter the number:"))
if age>=18:
    print("You are eligible to vote")
else:
    print(f"you have to wait {18-age} more years")
'''
eval:
eval() is a built-in Python function that evaluates a given expression(written as a string) and returns the result.'''
v=eval(input("Enter: "))
print(type(v))
print(v)



