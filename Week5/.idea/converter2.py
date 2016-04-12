def converter(celciusValue):
    fahrenheitValue = celciusValue * 9 / 5 + 32
    return fahrenheitValue

celciusValue = float(input('Enter the temperature in celcius:'))

print(converter(celciusValue))