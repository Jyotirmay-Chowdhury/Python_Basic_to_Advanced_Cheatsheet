# Python Variables (Crearing variables)
x = 6
y = "Jyotirmay"
print(x)
print(y)

# Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)

# Variable Names:- 
"""myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"""

# Multi Words variables Names:- 

# Camel Case 
A = myVariableName = "Joyotirmay"

# Pascal Case
B = MyVariableName = "Jyotirmay"

# Snake Case
C = my_variable_name = "Joyotirmay"

print(A,B,C)

# Assgn Multiple Values Variable

# Many Values to Multiple Variables

d, e, f = "Orange", "Banana", "Cherry"
print(d)
print(e)
print(f)

# One Value to Multiple Variables

g = h = i = "Orange"
print(g)
print(h)
print(i)

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
j, k, l = fruits
print(j)
print(k)
print(l)

# Python - Output Variables

m = "Python is awesome"
print(m)

# In the print() function, you output multiple variables, separated by a comma:

n = "Python"
o = "is"
p = "awesome"
print(n, o, p)

# You can also use the + operator to output multiple variables:

q = "Python "
r = "is "
s = "awesome"
print(q + r + s)

# Python - Global Variables

# -> Create a variable outside of a function, and use it inside the function

t = "awesome"

def myfunc():
  print("Python is " + t)

myfunc()

# Another Example of Python - Global Variables

u = "awesome"

def myfunc():
  u = "fantastic"
  print("Python is " + u)

myfunc()

print("Python is " + u)
