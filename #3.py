#1 
minutes = int(input()) 
hours = minutes // 60
remaining_minutes = minutes % 60
print(hours)
print(remaining_minutes)
#2
a = int(input())
b = int(input()) 
h = int(input())

if h < a:
    print("Недосып")
elif h > b:
    print("Пересып")
else:
    print("Это нормально")
#3

import math

a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
else:
    print("Треугольник не существует")
#4
import math

shape_type = input()

if shape_type == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(area)
elif shape_type == "прямоугольник":
    a = float(input())
    b = float(input())
    area = a * b
    print(area)
elif shape_type == "круг":
    r = float(input())
    pi = 3.14
    area = pi * r**2
    print(area)
else:
    print("Неизвестный тип фигуры")

#5
n = int(input())

if 11 <= n % 100 <= 14:
    word = "программистов"
elif n % 10 == 1:
    word = "программист"
elif 2 <= n % 10 <= 4:
    word = "программиста"
else:
    word = "программистов"

print(n, word)
#6
ticket_number_str = input()

sum_first_three = int(ticket_number_str[0]) + int(ticket_number_str[1]) + int(ticket_number_str[2])
sum_last_three = int(ticket_number_str[3]) + int(ticket_number_str[4]) + int(ticket_number_str[5])

if sum_first_three == sum_last_three:
    print("Счастливый")
else:
    print("Обычный")




