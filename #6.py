# 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("matrix:")
for row in matrix:
    print(row)
print("нечётные числа matrix")
odd_numbers = []
for row in matrix:
    for item in row:
        if item % 2 != 0:
            odd_numbers.append(item)
print(*(odd_numbers))
even_count = 0
for row in matrix:
    for item in row:
        if item % 2 == 0:
            even_count += 1
print(f"кол-во чётных: {even_count}")
# 2
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]
rows = len(matrix_1)
cols = len(matrix_1[0])
answer_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]
print(answer_matrix)
for row in answer_matrix:
    row_sum = sum(row)
    print(f"{row} сумма строки: {row_sum}")
# 3
fruits = [
    ["Banana", "apple"],
    ["apricot", "Avocado"],
    ["lime", "lemon"],
    ["Mango", "grapes"],
]

print("Элементы, написанные с заглавной буквы:")
for row in fruits:
    for item in row:
        if item[0].isupper():
            print(item)
# 4
random_elements = [
    ["toy", "bee", "cheese", "ear"],
    [False, "word", "0110110", 10],
    ["happiness", "(」°ロ°)」", "luck", None],
    ["car", "<- code ->", 4.7, True],
]

print("Каждый второй элемент (строка) из random_elements:")
for index, element in enumerate(random_elements):
    if index % 2 != 0:
        print(f"Индекс: {index}, Элемент: {element}")
# 5
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []
for i in range(rows):
    row_list = []
    for j in range(cols):
        value = float(input(f"Введите значение элемента [{i}][{j}]: "))
        row_list.append(value)
    matrix.append(row_list)
print("Ваш двумерный массив:")
for row in matrix:
    print(row)
