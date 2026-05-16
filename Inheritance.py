'''
Inheritance
--------------
-->Inheriting the methods from the base to child.
Example:'''
class parent:
    pass
class child(parent):
    pass
'''    
single Inheritance
-----------------------
->single inheritance enables a derived class to inherit properties from a single parent class,thus enabling code reusability and the addition
of new features to existing code.
Example:'''
class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def bark(self):
        print("Dog bark")
D=dog()
D.sound()
D.bark()
'''
Multiple inheritance
--------------------------
-->A child class inherits more than one class is called inheritance.
Example 1:'''
class Father:
    def skill_1(self):
        print("Driving")
class Mother:
    def skill_2(self):
        print("Cooking")
class child(Father,Mother):
    def All_skills(self):
        print("Coding")
C=child()
C.skill_1()
C.skill_2()
C.All_skills()
'''
Example 2:
--------------'''
class Python:
    def skill_1(self):
        print("Concept")
class DSA:
    def skill_2(self):
        print("Logical thinking")
class Aptitude:
    def skill_3(self):
        print("Calculation")
class child(Python,DSA,Aptitude):
    def All_skills(self):
        print("Problem solving")
C=child()
C.skill_1()
C.skill_2()
C.skill_3()
C.All_skills()
'''
Multi-level Inheritance:
-----------------------------
->Inherits from another child class
Example:'''
class grandfather:
    def house(self):
        print("Grandfather's house")
class father(grandfather):
    def land(self):
        print("Father's land")
class child(father):
    def flat(self):
        print("Son's flat")
s=son()
s.house()
s.land()
s.flat()
'''
Hierarchical inheritance:
--------------------------------
->multiple child classes inherits from one base class.
Example:'''
class father:
    def property(self):
        print("Father Property")
class child_1(father):
    def car(self):
        print("first child car")
class child_2(father):
    def flat(self):
        print("Second child flat")
c1=child_1()
c2=child_2()
c1.property()
c1.car()
c2.property()
c2.flat()
'''
Hybrid inhetitance:
-------------------------
Hybrid inheritance is a combination of more than one type of inheritance.It uses a mix lik single,multiple,or multilevel inheritance within the
same program.Python's method resolution order handle such situations.
Example:'''
class A:
    def methodA(self):
        print("Class A")
class B(A):
    def methodB(self):
        print("Class B")
class C(A):
    def methodC(self):
        print("Class C")
class D(B,C):
    def methodD(self):
        print("class D")
any=D()
any.methodA()
any.methodB()
any.methodC()
any.methodD()
'''
super() method
--------------------
-->The super() method is used to call methods or constructor from the parent class.
Example:'''
class parent:
    def __init__self():
        print("Parent Constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
c=child()
























