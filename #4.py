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
#1
number = int(input())

if number < 0:
    pass 
elif number > 100:
    print("*")
else:
    print("*" * number)
#2
str2 = input()

if str1 == str2:
    print(True)
else:
    print(False)
#3
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
#1
number = int(input())

if number <= 0:
    number = 1

print(number - 1)
print(number)
print(number + 1)
#2
filename = input()
extension = filename.split('.')[-1]

if extension == "doc":
    print("Word file")
elif extension == "py":
    print("Python file") 
elif extension == "txt":
    print("Text file")
else:
    print("Unknown file type")
#3
a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("равносторонний")
elif a == b or a == c or b == c:
    print("равнобедренный")
else:
    print("разносторонний")
#1
text = 'important information in one line'
letter = input()

if letter in text:
    print(True)
else:
    print(False)
#2
side1 = float(input())
side2 = float(input())

area = side1 * side2

if side1 == side2:
    figure_type = "квадрат"
else:
    figure_type = "прямоугольник"

print(figure_type)
print(area)
#3
print("Как твои дела?")
user_response = input().lower()

if user_response in ["хорошо", "нормально", "отлично"]:
    print("😊")
elif user_response in ["плохо", "не хорошо", "..."]:
    print("😥")
else:
    print("😐")
