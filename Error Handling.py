'''
Error Handling:
--------------------
try:
----
->The try block,that will test a block of code for errors.
Example:'''
try:
    print(1)
except:
    print("It is handling type error")
'''
except:
----------
This block will handle the error,which are written in the try block.
Example:'''
try
    print(num)
except:
    print("It is handling type error")
'''
Types of errors:
---------------------
->value error
->zerodivision error
->index error
->type error
'''
'''
else keyword:
------------------
The else keyword to define a block of code to be executed if no error were raised.
Example:'''
try:
    print("Hai"+7)
except:
    print("It is handling some error")
else:
    print("No error")
'''
Different types of errors example:
--------------------------------------------
Example:'''
try:
    print("This"+" is banana")
    print(2)
except NameError:
    print("It is handling some name error")
except TypeError:
    print("It is handling some type error")
except IndexError:
    print("It is handling some IndexError")
else:
    print("There is no error")
finally:
    print("Always execute this")























