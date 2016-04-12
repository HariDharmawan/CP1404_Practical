def rectangle_calc(width, height):
    area = width * height
    return area

width = int(input('enter width:'))
height = int(input('enter height:'))

print("Area:", rectangle_calc(width,height))