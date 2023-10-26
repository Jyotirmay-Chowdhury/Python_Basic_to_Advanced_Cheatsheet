# Creating a Function
'''
In Python a function is defined using the def keyword:
'''

def my_function():
  print("Hello from a function")

# Calling a Function

'''
To call a function, use the function name followed by parenthesis:
'''
def my_function():
  print("Hello from a function")
my_function()

# Arguments

'''
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). 
When the function is called, we pass along a first name, which is used inside the function to print the full name:

'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

