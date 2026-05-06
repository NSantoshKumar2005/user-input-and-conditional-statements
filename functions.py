'''
function
----------
-->This is a block of code that can be reusable
-->A function can only run when it is called
-->def is the keyword is to define the function
Syntax :
----------
def func_name(parameters):
    --------------------
    --------------------
func_name(arguments)
Ex:
----'''
num=9
def even_odd(num):
    if num%2==0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
even_odd(num)
even_odd(120)
'''
Required Arguments:
----------------------------
-->A function must called with correct number of arguments,that means if function expects 2 arguments ,we have to call function with
2 arguments not less or not more.

Case study 1:
-----------------'''
def even_odd(num,num_2):
  print(num+num_2)
even_odd(1,2,1)'''
output:
---------
TypeError : even_odd() takes 2 positional arguments but 3 were given'''
'''
Case study 2:
------------------'''
def even_odd(num,num_2):
  print(num+num_2)
even_odd(1)'''
output :
---------
TypeError: even_odd() missing 1 required positional argument: 'num_2'
'''
'''
Default Arguments:
-------------------------
-->By default, value is taken from the calling function.

Keyword Arguments:
---------------------------
-->Here,we can send arguments with key = value syntax.By this,the order of  arguments does not matter.
Ex:'''
def even_odd(name,Class,section):
    print(f"hai {name},{Class},{section}")
even_odd(name="Abdul Kalam",Class="First Class",section="A")
'''
Variable Length Argument:
-----------------------------------
-->Adding a star(*) before the parameter name in the function,receive a tuple of arguments and can be access items with indexes.
Ex:'''
def even_odd(*name):
    print(name[1])
even_odd("Abdul Kalam","Class","section")




