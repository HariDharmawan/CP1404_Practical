from guitar import Guitar
guitars = []
print("My Guitars!")

while True:
    name = input("Name:")
    if name =="":
        break
    year = int(input("Year:"))
    cost = float(input("Cost:"))
    print("{} ({}) : ${} is added".format(name,year,cost))
    guitars.append(Guitar(name, year, cost))

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(Vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))