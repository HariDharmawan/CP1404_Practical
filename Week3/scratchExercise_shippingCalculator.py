num_item = int(input("Enter the number of items: "))
while num_item < 0:
    print("Invalid number of items!")
    num_item = int(input("Enter the number of items: "))
else:
    ship_cost = int(input("Enter the shipping cost: $"))
    total_shipping_cost = num_item * ship_cost
    if total_shipping_cost > 100:
        discount = total_shipping_cost * 0.1
        final_cost = total_shipping_cost - discount
        print("10% DISCOUNT")
        print("$", final_cost)


