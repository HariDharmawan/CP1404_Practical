from guitar import Guitar

Gibson = Guitar("Gibson L-5 CES" , 1922, 16035.40)
Hendjai = Guitar("Hendjai L-4 DUN", 2010, 16035.40)
print(Gibson)
print(Gibson.get_age())
print(Gibson.is_vintage())
print(Hendjai)
print(Hendjai.get_age())
print(Hendjai.is_vintage())