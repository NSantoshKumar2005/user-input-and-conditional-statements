'''Removing Duplicates:
------------------------------
'''
l1=eval(input("Enter items:"))
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
'''
Finding Maximum number:
-----------------------------------'''
num=list(map(int,input("Enter a list:").split()))
largest=num[0]
for x in num:
    print(x,end=" " )
    if x>largest:
        largest=x
print("\nm:",largest)
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
            if Withdraw_M<=Teja_Ac_details['Balance'] and Withdraw_M:
                Teja_Ac_details['Balance']-=Withdraw_M
                print("Pls wait unlike money process")
            else:
                print("Insuff funds or change is not getable")
    else:
        print("Pls enter correct pin")
else:
    print("Pls enter only 4 digit pin")
























