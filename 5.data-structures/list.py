# list

fruits = ['apple','mango','melon'] 
# add 1 new single element
fruits.append('tangerine')
# add multiple element
fruits.extend(['watermelon','banana'])
# inserting element on a spesific index
fruits.insert(0,'jackfruit')
# delete element
fruits.remove('apple')
# delete element on a spesifi
fruits.pop(1) # mango deleted

fruitscopy = fruits.copy()
# delete all the elements
fruitscopy.clear()
"""
"Return the index value of the element that is the same as the input argument.
(Will return an error if the element does not exist.)"
"""
print(fruits.index('tangerine'))
# reverse element
fruits_r = fruits.copy()
fruits_r.reverse()
print(fruits_r)
# count the element
print(fruits.count('melon'))
# sort the list (lowest -> biggest)
s = [5,2,1,3,4]
s_r = s.copy()
s.sort()
print(s)
# sort the list (bigest -> lowest)
s_r.sort(reverse=True)
print(s_r)
print(fruits)
# del statement

del fruits[0] # delete index 0 element

# slicing

new_fruits = fruits.copy()
print(new_fruits[2:4])
del new_fruits[2:4]
print(new_fruits)
del new_fruits
# print(new_fruits) -> ERROR
print(fruits)
print(fruitscopy)
