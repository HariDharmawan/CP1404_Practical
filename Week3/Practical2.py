'''
text = input("Gender (M/F): ") # gender
if text == "M":
    print("Male")
else:
    print("Female")


sales = float(input("Enter Sales: $")) # sales
if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales *0.15
print("Bonus is $", bonus, sep='')


name = input("Name: ") #name
while name != "":
    print("hello", name)
    name = input("Name: ")
print("Goodbye")


for i in range(1,21,2): #range
    print(i, end=' ')
print()


for i in range(0,100,10): #range 10 to 100
    print(i, end=' ')


for i in range(20,0,-1): #range 20 to 1
    print(i, end=' ')
'''

