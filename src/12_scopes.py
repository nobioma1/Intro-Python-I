# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def changeX():
    global x # get to view x in function scope globally
    x = 99

changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x) # adding 'global x' to the changeX function


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y # get to view y in function scope in outer function scope
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y) # adding 'non local y' to the inner function

outer()