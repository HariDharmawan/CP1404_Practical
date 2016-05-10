from programminglanguage import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(vb)

    print("The dynamically typed languages are:")
    list = [python, vb, ruby]
    for each in list:
        if each.is_dynamic():
            print(each.name)

main()