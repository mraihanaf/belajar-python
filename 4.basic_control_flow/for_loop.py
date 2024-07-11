print("==For Loop==")
for i in range(3):
    print("for loop range(3)",i)
    
print()

for i in range(1,4):
    print("for loop range(1,4)",i)

print()

for i in range(0,6,2):
    print("for loop range(0,6,2)",i)

print()

fruits = ["banana","apple","mango"]
for fruit in fruits:
    print(fruit,"in fruits")

print()

data_str = "banana"
for letter in data_str:
    print("in string",letter)

print()

users = {"Udin": "online", "Asep":"offline","Budi":"online"}
print(users)
# Iterate over a copy
for user,status in users.copy().items():
    if status == "offline":
        print(user,"is offline")
        del users[user]

print(users)
# create new dict
active_users = {}
for user,status in users.items():
    if status == "online":
        active_users[user] = status

print("active_users:",active_users)