name = input("Enter your name: ")
menu = "(H)ello\n(G)oodbye\n(Q)uit"

print(menu)
choices = input("Enter your choices: ").upper()
while choices != "Q":
    if choices == "H":
        print("Hello", name)
        print(menu)
        choices = input("Enter your choices: ").upper()
    elif choices == "G":
        print("Goodbye", name)
        print(menu)
        choices = input("Enter your choices: ").upper()
    else:
        print("Invalid Message")
        print(menu)
        choices = input("Enter your choices: ").upper()
else:
    print("Finished")