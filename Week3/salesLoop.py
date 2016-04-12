sales = float(input("Enter Sales: $")) # sales
while sales < 0:
    if sales < 1000:
        bonus = sales * 0.1
        print("Bonus is $", bonus, sep='')
        sales = float(input("Enter Sales: $"))
    else:
        bonus = sales *0.15
        print("Bonus is $", bonus, sep='')
        sales = float(input("Enter Sales: $"))
else:
    print("Goodbye")