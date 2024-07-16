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

# Positional & Keyword arguments
def pos_kwd(param1, *param2, **param3):
    print("param1",param1) # param1 takes the first argument
    print("param2 positional",param2) # param2 takes all the positional arguments
    print("param3 keyword",param3) # param3 takes all the keyword arguments

pos_kwd("Halo","nama","saya",firstName="Udin",lastName="Sigma")

# Positional argument cannot appear after keyword arguments
# pos_kwd("Halo","nama","saya",firstName="Udin",lastName="Sigma","Weladahlah") --> error

# Positional only & Keyword only argument
def pos_only(arg, /):
    print(arg)

def kwd_only(*, arg):
    print(arg)

pos_only("positional argument")
# pos_only(arg="Hello") # this will return error.
kwd_only(arg="keyword argument")
# kwd_only("Hello") # this will return error

# combined
def combined_example(standard, pos_only, /, *, kwd_only):
    print("combined",standard,pos_only,kwd_only)

combined_example(1,2,kwd_only=3)

# Function annotations

# def function(var: data-type) -> data-type
# example

def addTwoNum(n1: int, n2) -> int:
    return n1 + n2

def sum(*numbers: int) -> int:
    out = 0
    for n in numbers:
        out += n
    return out

print("annotations addTwoNum() ->", addTwoNum(1,2))
print("annotations sum() ->", sum(1,2,3))
