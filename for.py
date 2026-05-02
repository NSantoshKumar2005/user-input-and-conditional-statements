'''range()
---------
-->This range() will generate sequence numbers upto the limit
syntax-->range(starting,ending,step)

Ex:'''
choice_U=int(input("Enter the limit:"))
for j in range(100,choice_U+1,3):
    print(j)
'''Even and Odd using range'''
for i in range(2,101):
    if i%2==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")
'''
break
-------
-->This break statement will exit if the condition becomes true,and never enters into next loops
Ex:'''
any=["Ganesh","Anish"]
for i in any:
    print(i)
    if i=="Sai":
        break
'''
continue:
-----------
-->This statement will skip that particular iteration and goes to next iterations.
Ex:'''
any=["Ganesh","Anish"]
for i in any:
    print(i)
    if i=="Ganesh":
        continue
    print(i)
'''
pass
------
-->pass is space holder,holds the space not to get any error
Ex:'''
a=9
b=90
if a>=b:
    pass
'''
Nested loop:
----------------
-->A loop in side the loop is called nested loop.
Ex:'''
for j in range(2,10):
    count=0
    for an in range(1,j+1):
        if j%an==0:
            count+=1
    if count==2:
        print(f"{j} is a prime")
    else:
        print(f"{j} is not a prime")
'''Ex:'''
num=int(input("Enter a number: "))
cou=0
for an in range(1,num+1):
    if num%an==0:
        cou+=1
if cou==2:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")'''







