#1
number = int(input()) 

if number < 0:
    number = abs(number) 
elif number == 0:
    number = 1


print(number)
#2
input_string = input()

if '.' in input_string or ',' in input_string:
    print(True)
else:
    print(False)
#3
num1 = int(input())
num2 = int(input())

div1 = num1 % 3 == 0
div2 = num2 % 3 == 0

if div1 and div2:
    print(True)
elif div1 or div2:
    print("Одно число делится на 3")
else:
    print(False)
#4
number = int(input())

if number < 0:
    pass 
elif number > 100:
    print("*")
else:
    print("*" * number)
str2 = input()

if str1 == str2:
    print(True)
else:
    print(False)
#6
r = int(input())
g = int(input())
b = int(input())

if r == 0 and g == 0 and b == 0:
    print("Чёрный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зелёный цвет")
elif r == 0 and g == 0 and b == 255:
    print("Синий цвет")
else:
    print("Нет цвета")


