'''
Finding Even and Odd in the given list using recursion
'''
any=[34,67,56,2,3,7]
def even_odd(any):  
    for j in any:
        if j%2 == 0:
            print("Even:",j)
        elif j % 2 != 0:
            print("Odd: ",j)
even_odd(any)
'''
Fibonacci Series for a given parameter :
--------------------------------'''
def recursion(n):
    if n<=1:
        return n
    else:
        return recursion(n-1)+recursion(n-2)
print(recursion(2))

'''
Armstrong Number for a given number:
-------------------------------------'''
Armstrong_=153
total=0
length_=len(str(Armstrong_))
for j in str(Armstrong_):
    total=int(j)**length_
if total==Armstrong_:
    print(f"{Armstrong_} is a Armstrong number")
else:
    print(f"{Armstrong_} is not a Armstrong number")
'''
Finding the given value is divisible by 3 and 5:
-------------------------------------------------------------'''
num=100
def Divi_(num):
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print(f"{i} is divi by 3 and 5")
Divi_(num)
'''
Lambda Function:
------------------------
-->A lambda function is a small anonymous function
-->This lambda function can take n number of arguments but can only have one expression.

syntax --> lambda keyword(arguments) : expression

Example : Multiplication of Two numbers'''
an=lambda a,b:a*b
print(an(5,6))
































