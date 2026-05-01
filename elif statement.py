'''
elif statement
-----------------
-->This statement gives more options to get result of that program
Ex:'''
marks_stu=int(input("Enter your marks:"))
if marks_stu>=90:
    print("A+")
elif marks_stu>=80:
    print("B+")
elif marks_stu>=60:
    print("B")
elif marks_stu>=50:
    print("C+")
else:
    print("Failed")
'''
Nested if statement
--------------------------
-->if statement in side another if statement is called nested if statement
Ex:'''
user_SBI_info={"ATM PIN":"7700"}
User_pin=input("Enter your ATM:")
if len(User_pin)==4:
    if User_pin in user_SBI_info['ATM PIN']:
        print("welcome to SBI ATM")
    else:
        print("Pls enter the correct pin")
else:
    print("Pls entere 4 digit pin")
'''
for statement
-----------------
-->A for statements is used to iterate over like (string,list,tuple) with fixed number of iterations
'''
'''
else statement in for
--------------------------
-->after completing all iterations this else statement will execute
Ex :'''
any=[23,45,6,7,8]
for j in any:
    print(j)
else:
    print("Loop finished")
'''
while statement
--------------------'''
v=1
while v<=5:
    print(v)
    v+=1

palindrome
--------------
so="madam"
empty_=""
for j in so:
    empty_=j+empty_
if empty_==so:
    print("palindrome")
else:
    print("Not a palindrome")

'''








