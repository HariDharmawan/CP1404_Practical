def bmiCalc(weight, height):
    calculate = weight / height ** 2
    return calculate
    print('Therefore, your BMI value is:', bmi)

weight = int(input('Enter your weight in kilograms:'))
height = float(input('Enter your height in meters:'))

print(bmiCalc(weight,height))