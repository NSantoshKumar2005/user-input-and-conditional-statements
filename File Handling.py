'''
File Handling :
--------------------
-->File handler is an object of a file to maintain several function of file like creating,reading,updating and
deleting the files...
Two ways to open
------------------------
1.open():
------------
syntax:
filehandler=open("filename.txt","mode")
print(filehandler)

close():
----------
syntax:
any=open("demo.txt","r")
any.close()

2.with open()
------------------
syntax->
with open("filename","mode") as file handler:
Example:'''
with open("demo.txt","r") as so:
    print(so.read())
'''
with keyword:
------------------
-->Using this with keyword no need close the file in the lines,it will close the file automatically.

Modes:
----------
r-->Used to the file and throw error if the file does not exist ...
a-->Used to add the text at last,if the file does not exist it will create.
w-->Used to add new text as override the text in the file,if the file does not exist it will create.
x-->Used to create the file and throw error if the file exist.
Example:'''
with open("In.txt","w") as so:
    print(so.write("This is"))
    print(so.read())
'''
read():
---------
-->This read method can read the entire file chunk by chunk where can special size.
Example:
-------------'''
with open("demo.txt","r") as so:
    print(so.read(2))
'''
readline():
--------------
-->This method can read one line at a time
Example:'''
with open("demo.txt","r") as so:
    print(so.readline())

with open("demo.txt","r") as so:
    print(so.readlines())

with open("demo.txt","a") as so:
    print(so.write("SomeThing"))

with open("demo.txt","w") as so:
    print(so.write("Something"))
'''
























