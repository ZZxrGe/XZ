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
#1
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if a > b:
    result = a ** b
elif b > a:
    result = b ** a
else:
    result = a + b
print(f"Результат: {result}")
#2
new_message = "Hello! How are you?"
user_response = input("Введите ваш ответ: ")

if new_message and user_response:
    is_same_start = new_message[0] == user_response[0]
    print(f"Результат: {is_same_start}")
else:
    print("Ошибка: одна из строк пуста.")
#3
length1 = float(input("Введите длину первого отрезка: "))
length2 = float(input("Введите длину второго отрезка: "))

if length1 > length2:
    difference = length1 - length2
    print(f"Первый отрезок длиннее второго на {difference}")
elif length2 > length1:
    difference = length2 - length1
    print(f"Второй отрезок длиннее первого на {difference}")
else:
    print("Отрезки равны по длине.")
#1
user_string = input("Введите строку: ")

if user_string:
    is_same_ends = user_string[0] == user_string[-1]
    print(f"Результат: {is_same_ends}")
else:
    print("Ошибка: строка пуста.")
#2
number = float(input("Введите число: "))
if number % 2 == 0:
    result = number ** 2
elif number % 3 == 0:
    result = number ** 3
else:
    result = number * 100
print(f"Результат: {result}")
#3
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 < 0:
    num1 += 1000
    print(f"Первое число изменено: {num1}, Второе число: {num2}")
if num2 < 0:
    num2 += 1000
    print(f"Второе число изменено: {num2}, Первое число: {num1}")
if num1 < 0 and num2 < 0:
    print(False)
elif num1 >= 0 and num2 >= 0:
    print(True)
num1_orig = float(input("Введите первое число: "))
num2_orig = float(input("Введите второе число: "))

if num1_orig < 0 and num2_orig < 0:
    print(False)
elif num1_orig >= 0 and num2_orig >= 0:
    print(True)
else:
    if num1_orig < 0:
        num1_modified = num1_orig + 1000
        print(f"Первое число изменено на {num1_modified}, второе: {num2_orig}")
    elif num2_orig < 0:
        num2_modified = num2_orig + 1000
        print(f"Второе число изменено на {num2_modified}, первое: {num1_orig}")
        #1
user_string = input("Введите строку: ")
vowels = ['я', 'и', 'е', 'ю']
if user_string and user_string[-1] in vowels:
    print(True)
else:
    print(False)
#2
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))
if a <= 0 or b <= 0 or c <= 0:
    print(False)
elif a + b > c and a + c > b and b + c > a:
    print(True)
else:
    print(False)
    #3
last_digit = number % 10
if last_digit == 0:
    result = number ** 10
elif last_digit == 1:
    result = number % 3
elif last_digit == 2:
    result = number // 2
else:
    result = number ** 2
print(f"Результат: {result}")
#1
number = int(input("Введите целое число: "))
last_digit = number % 10
if last_digit == 0:
    result = number ** 10
elif last_digit == 1:
    result = number % 3
elif last_digit == 2:
    result = number // 2
else:
    result = number ** 2
print(f"Результат: {result}")
#2
pc_number = 777
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if (num1 < pc_number and num2 > pc_number) or (num2 < pc_number and num1 > pc_number):
    print(True)
else:
    print(False)
#3
lamp_1 = 0
lamp_2 = 0
user_choice = input("Какую лампочку зажечь? ")
if user_choice == "1":
    lamp_1 = 1
    print(f"Лампочка 1 горит. Состояние: lamp_1={lamp_1}, lamp_2={lamp_2}")
elif user_choice == "2":
    lamp_2 = 1
    print(f"Лампочка 2 горит. Состояние: lamp_1={lamp_1}, lamp_2={lamp_2}")
else:
    print("Обе лампочки не горят")
#1
switch_1 = False
switch_2 = False
user_input = input("Включить? ")
if user_input.lower() == "да":
    switch_1 = True
    switch_2 = True
    print(f"Всё включено. Значения разъемов: switch_1={switch_1}, switch_2={switch_2}")
else:
    print(f"Изначальные значения разъемов: switch_1={switch_1}, switch_2={switch_2}")
#2
number = int(input("Введите число: "))
if number > 0:
    if number % 2 == 0:
        print("True, «even»")
    else:
        print("True, «odd»")
else:
    print(False)
#3
user_string = input("Введите строку: ")
if user_string and user_string[0] == '/':
    print("«command»")
else:
    print("«It's string>>>»")
#1
user_string = input("Введите произвольную строку: ")
length = len(user_string)
if length == 0:
    print("None")
elif length <= 5:
    print("«short»")
elif 6 <= length <= 10:
    print("«normal»")
else:
    print("«long»")
    #2
result = 0
if number < 0:
    number = 1000000
    result = number
elif number == 0:
    number = 2
    result = number ** 2
else:
    result = number ** 3
print(f"Результат: {result}")
#3
number_1 = 10
number_2 = 100
user_number = int(input("Введите своё число: "))

if number_1 < user_number < number_2:
    print(True)
else:
    print(False)
              









