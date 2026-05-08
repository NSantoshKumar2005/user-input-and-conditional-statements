'''
Print Statement:
------------------------
-->This print statement shows output on screen.

Return statement:
------------------------
-->sends a value back to the caller or calling function for the program to reuse.

Inbuilt functions:
---------------------
A)len() : This function is used to find out the number of values present in itterables.
example :'''
Printing values for the given numbers in a list.
list = [12,34,2,4,5]
for i in range(0,len(list)):
    print(list[i])
'''
B)max():
This is used to get the maximum value

example :'''
Printing values for the given string
list="Python is  a language"
print(max(list())
'''
Note:
-------
If the given types are different then max function cannot be worked and it will give type error.
Example:'''
m=("python",1)
print(max(m))
'''
C)min():
--------
This is used to get the maximum value.
Example:'''
list="Python is  a language"
print(min(list())
'''
D)type():
----------
This is used to represent what type of value the given variable value.
Example:'''
str="value"
print(type(str))
'''
D)range():
----------
-->The range() function is a built-in tool that generates a sequence of integers
-->It is used in for loops to repeat a block of code a specific number of times
Example:'''
for i in range(2):
    print(i)
'''
Recursive function:
-------------------------
A function call itself is called recursive function until a base case is stops it.

Example 1 :'''
Finding factorial of a given number
def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)
print(fact(2))
'''
Example 2 :
Printing the table'''
def table(num):
    for j in range(1,11):
        print(f"{num*j}")
    table(num=int(input("Enter a number:")))
'''


















