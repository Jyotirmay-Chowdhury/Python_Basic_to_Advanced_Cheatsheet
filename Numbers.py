# Python Numbers

'''
There are three numeric types in Python:

1) int
2) float
3) complex

'''

A = 1 
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

B = 2.8  
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

C = 1j   
# Complex numbers are written with a "j" as the imaginary part:

print(type(A))
print(type(B))
print(type(C))

# Type Conversion

#You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

