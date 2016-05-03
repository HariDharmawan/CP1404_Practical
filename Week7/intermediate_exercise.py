COLOUR_NAMES = {"Aliceblue":"#f0f8ff", "Antiquewhite": "#faebd7", "Antiquewhite1":"#ffefdb", "Antiquewhite2":"#eedfcc", "Antiquewhite3":"#cdc0b0", "Antiquewhite4":"#8b8378", "Aquamarine1":"#7fffd4", "Aquamarine2":"#76eec6", "Azure1":"#f0ffff", "Azure2":"#e0eeee"}

name = input("Enter colour name: ").capitalize()

while name != "":
    if name in COLOUR_NAMES:
        print(name, "is", COLOUR_NAMES[name])
    else:
        print("Invalid colour names")
    name = input("Enter colour names: ")
