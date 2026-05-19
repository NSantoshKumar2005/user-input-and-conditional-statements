'''
Polymorphism
-------------------
-->Polymorphism mean "many forms",The same method,operator or a function can perform different actions depending upon
the object or data type.

1.Method Overloading:
-------------------------------
->Method overloading is a feature of object-oriented programming where a class can have multiple methods with the same name
but different parameters.To overload method,we must change the number of parameters or the type of parameters or both.
->Python does not support the feature of method overloading by default.But their is way to achieve,if you define a method multiple times
the last definition will override the previous ones.

Example:'''
class Addition:
    def add(self,a,b=0,c=0):
        return a+b+c
obj=Addition()
print(obj.add(23,7))
print(obj.add(10,20,30))
class Power:
    def pow(self,a,b,b=2):
        return a**b
an=Power()
print(an.pow(5))
print(an.pow(10,3))
'''
Multiple method with different data
----------------------------------------------'''
class Addition:
    def add(self,a,b=0,c=0):
        return a+b+c
    def add(self,a,b=0,c=0,d=0):
        return a+b+c+d
obj=Addition()
print(obj.add(23,7))
print(obj.add(10,20,30,9))
'''
2.Method Overriding:
----------------------------
-->Method Overriding occur when a child class provides a different implementation of a method already present in the parent class.

Example:'''
class animal:
    def sound(self):
        print("Animals make sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
any=dog()
any.sound()
'''
3.Operator Overloading:
--------------------------------
Operator overloading allows same operator to work in different ways depending on data type.

Example:'''
class student():
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,any_):
        return self.marks+any_.marks
so=student(56)
how=student(78)
print(so+how)
'''
ABC(Abstract base class):
-----------------------------------
-->An abstract base class(ABC) is a class that can't be instantiated on its own and is designed to be a blueprint for other classes.
'''
Example:
from abc import ABC,abstractmethod
class vehical(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehical):
    def start(self):
        print("Car starts with key")
who=car()
who.start()
























    
