name = input("What Is Your Name?\n")

if name == "bob":
    askifheisevil = input("Are You Evil?\n")
    if askifheisevil == "yes":
        print("Get Out Now", name + "!\nYou Are Not Allowed Here!")
    elif askifheisevil == "no":
        print("Welcome", name)
else:
    print("Welcome", name)
