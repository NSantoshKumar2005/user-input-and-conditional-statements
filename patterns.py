'''
pattern programs
----------------------
printing the numbers in Right Angled Triangle:'''
num=int(input("Enter number:"))
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i,end=" ")
    print()

''' 
printing the stars in Right Angled Triangle:
--------------------------------------------------------'''
num=int(input("Enter number:"))
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*",end=" ")
    print()
'''
Reversing the Right Angled Triangle for numbers 
-----------------------------------------------------------------'''
num=int(input("Enter number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''  
printing the Pyramid
---------------------------'''
n=int(input("Enter number:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
''' 
Calculator Program
--------------------------'''
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
choice_=int(input("\n1.Add \n2.Sub \n3.Mul : \n  "))
if choice_==1:
    print(num_1+num_2)
elif choice_==2:
    print(num_1-num_2)
elif choice_==3:
    print(num_1*num_2)
elif choice_==-1:
    print(num_1**num_2)
elif choice_==-2:
    print(num_1/num_2)
elif choice_==-3:
    print(num_1//num_2)
else:
    print("Given option is not present") 




























