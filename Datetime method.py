'''Datetime method
-------------------------
To work with data and time
Example:'''
import datetime
today=datetime.date.today()
print(today)
'''
Example:'''
import datetime
now=datetime.datetime.now()
print(now.time())
'''
Common format code:
%d--------->Day
%m-------->Month
%Y---------->Year
%M---------->Min
%S----------->Sec

strftime()
------------
-->This used to format date and time
Example:
'''
import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M:%S"))
'''
Example:'''
import datetime
Dat_1=datetime.date(2026,1,26)
Dat_2=datetime.date(2026,2,26)
Diff=Dat_1-Dat_2
print(Diff.days)
'''
ATM APP form data submission - Create
Example:
'''
import datetime
any=datetime.datetime.now()
print(any.hour)
print(any.minute)
print(any.second)
print(any.microsecond)
