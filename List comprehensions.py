'''
ATM operations:
---------------------'''
Teja_Ac_details={"Name":"Teja","ATM PIN":"1212","Balance":3000}
print("--Welcome to ATM--")
print("Pls insert your card")
user_pin=input("Pls enter your 4 digit pin: ")
if len(user_pin)==4:
    if user_pin in Teja_Ac_details['ATM PIN']:
        Choice_=int(input("\n1.Withdraw \n2.Deposite: "))
        if Choice_==1:
            Withdraw_M=int(input("Enter amount you want to withdraw: "))
            if Withdraw_M<=Teja_Ac_details['Balance'] and Withdraw_M:%100==0:
                Teja_Ac_details['Balance']-=Withdraw_M
                print("Pls wait unlike money process")
            else:
                print("Insuff funds or change is not getable")
elif Choice_==2:
    Deposite_M=int(input("Pls enter amount you want to Deposite:"))
    if Deposite_M>=1000 and Deposite_M%100==0:
        Teja_SBI_AC_details['Balance']+=Deposite_M
        print("Your money deposited in AC")
        print(Teja_SBI_AC_details['Balance'])
    else:
        print("Pls deposite amount greater than 1000 or we are not accept change")
else:
    print("Pls enter correct pin")
else:
    print("Pls enter only 4 digit pin")
'''
List Comprehension:
----------------------------
-->List comprehension offers shorter syntax when we want to create a new list based on the values of an existing list.

syntax-->[expression loop condition]

Example:
old_l=[12,3,5,68,90]
New_l=[i if i%2!=0 else "even" for i in old_l]  
print(New_l)

Dictionary comprehension:
------------------------------------
-->Dict comprehension offers shorter syntax when we want to create a new dict based on the values of an existing dict.
Example:
an={"a":2,"b":3,"c":5,"d":8}
so={x:y  for (x,y) in an.items() if y%2==0 }
print(so)
'''

