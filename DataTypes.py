# Python has the following data types built-in by default, in these categories:

'''
1) Text Type:	str
2) Numeric Types:	int, float, complex
3) Sequence Types:	list, tuple, range
4) Mapping Type:	dict
5) Set Types:	set, frozenset
6) Boolean Type:	bool
7) Binary Types:	bytes, bytearray, memoryview
8) None Type:	NoneType
'''

# Data types ->

A = "Hello World"  # Print string
B = 20  # integer
C = 20.5 # float
D = 1j #complex number
E = ["Apple","Google","Microsoft"]
F = ("Apple","Google","Microsoft")
G = range(6)
H = {"Apple":"A","Iphone Model":"Iphone 15"}
I = {"Apple","Google","Microsoft"}
J = frozenset({"Apple","Google","Microsoft"})
K = True
L = b"Hello"
M = bytearray(5) 
N = memoryview(bytes(5))
O = None


#display:
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
print(I)
print(J)
print(K)
print(L)
print(M)
print(N)
print(O)

#display the data types:
print(type(A)) 
print(type(B))
print(type(C))
print(type(D))
print(type(E))
print(type(F))
print(type(G))
print(type(H))
print(type(I))
print(type(J))
print(type(K))
print(type(L))
print(type(M))
print(type(N))
print(type(O))