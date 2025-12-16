# 1
m = ["круг", 0.25, "квадрат", "треугольник", 15, "круг", "овал", "10"]
shapes = ["круг", "квадрат", "треугольник", "овал"]
i = 0
while i < len(m):
    if m[i] not in shapes:
        m.remove(m[i])
    else:
        i += 1

print(m)
# 2
abc = ["A", "B", "C", "D", "E", "F", "G"]
del abc[1:5]
print(abc)
# 3
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2, 3)
print(numbers)
# 4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
positive_mass = [n for n in mass if n >= 0]
positive_mass.sort()
print(positive_mass)
positive_mass.reverse()
print(positive_mass)
# 5
negatives = []
positives = []
zeros = []
try:
    count = int(input("Введите количество вводимых чисел: "))
    for _ in range(count):
        num = float(input(f"Введите число {_ + 1}: "))
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
        else:
            zeros.append(num)
    sum_negatives = sum(negatives)
    print(f"Сумма отрицательных чисел: {sum_negatives}")
    if positives:
        average_positives = sum(positives) / len(positives)
        print(f"Среднее арифметическое положительных чисел: {average_positives}")
    else:
        print("Положительные числа отсутствуют, среднее арифметическое не вычислялось.")
    zeros_with_stars = ["*" for _ in zeros]
    print(f"Количество нулей (заменены на *): {len(zeros)}")
    print(f"Список нулей: {zeros_with_stars}")
except ValueError:
    print("Ошибка ввода. Пожалуйста, вводите только числа.")
