'''
Class:
--------
-->class is instance or blueprint of an object.
Example:'''
class student:
    def display(self):
        print("Hello")
'''
Object
--------
-->object is the instance of the class
Example:'''
class car:
    def brand(self):
        print("I have created a new car")
Car_1=car()
Car_1.brand()
'''
Constructor
----------------
-->A constructor is a special method that executes automatically when the object is created
-->(__init__)
Example:'''
class car:
    def __init__(self,color,Brand):
        self.color=color
        self.Brand=Brand
    def car_brand(self):
        print(f"Brand is {self.Brand}")
    def car_color(self):
        print(f"color is {self.color}")
Car_1=car("Blue","BMW")
Car_1.car_brand()
'''
self keyword
----------------
-->This self refer to the current object
Example:'''
class student:
    def __init__(self,name,age,gender,year):
        self.name=name
        self.age=age
        self.gender=gender
        self.year=year
    def student_det(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.year)

    def student_year(self):
        print(self.year)
stu_=student("Teja",1,"Male",2030)
stu_.student_det()
stu_.student_year()
'''
Encapsulation:
--------------------
-->This means binding data and the methods that works on the data inside the class,while limiting direct access to the internal state.
Points to remember:
->name is public and can be accessed directly.
->Adhar is a procted,means internal use only.
->Pan is  a private, this makes direct access hard.
'''
class bank:
    def __init__(self,name,Adhaar,Pan):
        self.name=name
        self._Adhaar=Adhaar
        self._Pan=Pan
    def Adhaar_(self):
        print(self._Adhaar)
    def Pan_(self):
        print(self._Pan)

SBI_bank=bank("Teja",123123123,"GPRKKMKBHFD")
SBI_bank.Adhaar_()













































    
