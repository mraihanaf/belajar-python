# basic data types
thisIsStr = "RAWR"
thisIsNumber = 123
thisIsFloat = 1.2
thisIsBool = True
thisIsBoolF = False
thisIsDict = {"foo":"bar"}

print(thisIsDict["foo"])

# list, tuple, frozenset
thisIsList = [1,'List',True]
thisIsTuple  = (1,'Tuple',True)

# Difference

print(thisIsList) # mutable
print(thisIsTuple) # immutable

# thisIsTuple[0] = 2 <-- ERROR!
thisIsList[0] = 2
print(thisIsList)

# set artinya himpunan

thisIsSet = {"apple","mango","set"}
thisIsFrozenSet = frozenset(thisIsSet)

# diiference

thisIsSet.add("cherry")
# thisIsFrozenSet.add("cherry") <-- ERROR! 

print(thisIsSet)
print(thisIsFrozenSet)
