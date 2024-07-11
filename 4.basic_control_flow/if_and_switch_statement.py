print("==IF Statements==")
x = int(input("Masukan Integer : "))
if x < 0:
    print("Integer lebih kecil dari 0")
elif x == 0:
    print("Zero.")
elif x == 1:
    print("Single.")
else:
    print("More.")

# Match case statements
print("==Match Statements==")
match x:
    case x if x < 0:
        print("Integer lebih kecil dari 0")
        # Match statements tidak bisa pake continue,break kayak di c++ :/       
    case 0:
        print("Zero.")
    case 1:
        print("Single")
    case 2|3|4:
        print("WOAH!")
    case _:
        print("More")
