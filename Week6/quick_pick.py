import random
user_input = int(input("How many quick picks?"))

for i in range(user_input):
    numbers = []
    for i in range(6):
        while True:
            rand_num = random.randint(1,45)
            if rand_num in numbers:
                rand_num = random.randint(1,45)
            else:
                numbers.append(rand_num)
                break
    numbers.sort()
    print("{:2d}, {:2d}, {:2d}, {:2d}, {:2d}".format(numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5]))