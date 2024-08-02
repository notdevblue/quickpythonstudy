# https://docs.python.org/3/tutorial/controlflow.html#defining-functions

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(2000)

# def introduces a function definition
# must be followed by the funciton name and paranter-sized list of formal parameters

# first statement of the funcion body can optionally be a string literal
# this is the function's documentation string (or docstring)
# there are tools which use docstrings to automatically produce online or printed documentation.
# or let user interactively browse through code. (it's a good practice so make a habit of it.)

# all variable assignments in a function store the value in the local symbol table.
# global variables and variables of enclosing function cannot be directly assigned a value within a function
# (unless global variables named in a global statement, or for variables of enclosing function named in a nonlocl statement)

# global_variable = 1 # have to put global to make assignment below work.

# def fun():
#    global_variable = 10 # global_variable is not accessed
#
# fun()

# print(global_variable)

# arguments are passed using call by value.

# and you can do below things.
# interpreter recognizes the object pointed to by that name.

f = fib
f(100)
print(id(f) == id(fib)) # >>> True

# you might object that fib is not a function but a procedure since it doesn't return a value.
# In fact, even function without a return statement do return a value, called None. It's normally suppressed by the interpreter.

print(f(0)) # >>> None

def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib2(100)
print(f100)

# return without an expression argument returns None. Fallong off the end of a function also returns None.

# result.append(a) calls a method of the list object result.
# method is a function that 'belongs' to an object and is named obj.methodname, where obj is some object (this may be an expression) and methodname is the name of a method that is defined by the object's type.
# append() adds a new element at the end of the list.
