f3=open('hello.py','r')
for x in f3:
    print(x)

f2=open("Create_File.py",'r')
print(f2.read())
print(f2.read(2)) 
print(f2.read(2)) 
print(f2.read(3))
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.readlines())
d=f2.readlines()
print(type(d))    

import os
print(os.getcwd())

import os
os.mkdir('4pm batch')
os.rmdir('4pm batch')
os.remove('josh940Am.txt')
print(os.path.exists('Josh2pm.txt'))
print(os.path.exists('Josh.txt'))
print(os.path.exists('2pm BaTch'))