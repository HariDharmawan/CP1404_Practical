def get_number(firstInput, SecondInput):
    while firstInput > secondInput:
        print("Please enter a valid number!")
    while s

lower = 10
upper = 100

firstInput = int(input("Enter a number {}-{}:".format(lower,upper)).strip())
secondInput = int(input("Enter a number {}-{}:".format(lower,upper)).strip())

for i in range(firstInput,secondInput):

    print("{} {}".format(i, chr(i).strip()))
