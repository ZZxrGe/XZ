# 1
matrix = [
    ["folder", "coursework.doc", "folder", "pict.png", "data.accdb"],
    ["icon.ico", "script.js", "index.html", "style.css", "prog.py"],
    ["my_song.mp3", "anapa-2003.jpg", "cs_1.6.exe", "folder", "cheat.txt"],
    ["notes.txt", "main.py", "work.pdf", "cartoon.mp4", "array.py"],
    ["project.psd", "cycle.py", "folder", "cycle.js", "turtle.py"],
]

print("начальный список")
for row in matrix:
    print(row)
matrix_cleaned = []
for row in matrix:
    cleaned_row = []
    for item in row:
        if item != "folder":
            if item == "data.accdb":
                cleaned_row.append("data.sql")
            else:
                cleaned_row.append(item)
    matrix_cleaned.append(cleaned_row)

print("\nбез папок и с заменой data")
for row in matrix_cleaned:
    print(row)
py_files = []
for row in matrix:
    for item in row:
        if item.endswith(".py"):
            py_files.append(item)

print("\nвсе файлы.py")
print(*(py_files))
js_files = []
for row in matrix:
    for item in row:
        if item.endswith(".js"):
            js_files.append("new_" + item)

print("\nвсе new_файлы.js")
print(*(js_files))
# 2
word_numb = [
    "ноль",
    "один",
    "два",
    "три",
    "четыре",
    "пять",
    "шесть",
    "семь",
    "восемь",
    "девять",
]
try:
    n_input = int(input("Введите число n от 0 до 9: "))
    if 0 <= n_input <= 9:
        print(f"Элементы списка от 0 до {n_input}:")
        for i in range(n_input + 1):
            print(word_numb[i])
    else:
        print("Введите число <= 9")
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите целое число.")
# 3
bin_sy = ["11011111", "11011101", "11000111", "11011100", "11011110"]
decimal_numbers = []
print("Десятичные числа:")
for binary_str in bin_sy:
    decimal_num = int(binary_str, 2)
    decimal_numbers.append(decimal_num)
    print(decimal_num)
max_num = max(decimal_numbers)
min_num = min(decimal_numbers)
print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
# 4
A = [[-446, 281, -80], [465, 432, -122], [13, "error", 8]]
for i, row in enumerate(A):
    for j, item in enumerate(row):
        if isinstance(item, str):
            A[i][j] = len(item)

print("Исправленная матрица А:")
for row in A:
    print(row)
total_sum = 0
for row in A:
    total_sum += sum(row)
print(f"Сумма всех элементов матрицы: {total_sum}")
# 5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_sum = 0
n = len(matrix)
for i in range(n):
    j = n - 1 - i
    diagonal_sum += matrix[i][j]
print(f">>> {diagonal_sum}")
