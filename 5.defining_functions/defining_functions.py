# Defining function

def sayHello():
    """Print Hello to the terminal"""
    print("Hello")

sayHello()

# arguments
# argument can be single or more
def sayHelloTo(firstname,lastname):
    print(f"Hello {firstname} {lastname}!")

sayHelloTo("Udin","Sigma")

# default arguments values
def printNumber(default=10):
    print(default)

printNumber()
printNumber(5)

def doNothing():
    pass # pass statement can be used in the function too
doNothing()

# mutable default values (e.g., lists) are evaluated only once. 
# this affects functions that accumulate arguments, as shown in the example below.
def accumulate_args(arg,list=[]):
    list.append(arg)
    return list

# example usage
print("accumulate_args",accumulate_args(1)) # output -> [1]
print("accumulate_args",accumulate_args(2)) # output -> [1,2]
print("accumulate_args",accumulate_args(3)) # output -> [1,2,3]

# to solve this problem we can use None as a default 
def f(arg,L=None):
    if L is None:
        L = []
    L.append(arg)
    return L

print("solved",f(1)) # -> [1]
print("solved",f(2)) # -> [2]
print("solved",f(3)) # -> [3]

