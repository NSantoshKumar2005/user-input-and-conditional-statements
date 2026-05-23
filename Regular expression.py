'''
Regex or Regular Expression is a sequence of char that forms a searching pattern.
Functions
--------------
findall()
search()

Example:'''
import re
some="Python is a language."
any=re.findall("[a]",some)
print(any)
'''
Example:'''
import re
some="Python is a language."
any=re.search("[a]",some)
print(any)
'''
Metacharacters
---------------------
->[]-->A-Z,a-z,[ahg]
Example:
'''
import re
some="Python is a language."
any=re.findall("[a]",some)
print(any)
'''
^-->checks the string is starting with or not .
Example:'''
import re
some="Python is a language."
any=re.findall("^Python",some)
print(any)
'''
$ ->
Example:
'''
import re
some="Python is a language."
any=re.findall("language.$",some)
print(any)
'''
* -> zero to n number of char
Example:
'''
import re
some="Python is a language"
any=re.search("P.*n",some)
print(any)
'''
+ ->
Example:
'''
import re
some="Python is a language"
any=re.search("P.+thon",some)
print(any)
'''
{} ->
Example:
'''
import re
some="Python is a language"
any=re.findall("P.{10}",some)
print(any)











