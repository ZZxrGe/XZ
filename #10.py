# 1
def upper_func(t):
    """Выводит только заглавные буквы из строки t."""
    result = ""
    for char in t:
        if char.isupper():
            result += char + " "
    print(result.strip())


print(">>> upper('PriVet')")
upper_func("PriVet")
print(">>> upper('hello world')")
upper_func("hello world")


# 2
def punct(txt):
    """Считает количество знаков препинания в строке."""
    count = 0
    punctuation_chars = "!?. ,()"
    for char in txt:
        if char in punctuation_chars:
            count += 1
    print(count)


print(">>> punct('(Как дела?)')")
punct("(Как дела?)")


# 3
def create_cube(x, y):
    """Рисует прямоугольник из звездочек размером x на y."""
    for _ in range(y):
        print("*" * x)


print(">>> create_cube(5, 3)")
create_cube(5, 3)


# 4
def double(s):
    """Удваивает каждый символ в строке."""
    result = ""
    for char in s:
        result += char * 2
    print(result)


print(">>> double('строка')")
double("строка")


# 5
def Constructor(details, people, cars, trees):
    """Рассчитывает максимальное количество полных наборов."""
    required_details = 72
    required_people = 4
    required_cars = 2
    required_trees = 7
    max_sets = min(
        details // required_details,
        people // required_people,
        cars // required_cars,
        trees // required_trees,
    )
    print(max_sets)


print(">>> Constructor(144, 8, 4, 14)")
Constructor(144, 8, 4, 14)
print(">>> Constructor(10000, 16, 6, 2)")
Constructor(10000, 16, 6, 2)


# 6
def Constructor(details, people, cars, trees):
    """Рассчитывает максимальное количество полных наборов."""
    required_details = 72
    required_people = 4
    required_cars = 2
    required_trees = 7
    max_sets = min(
        details // required_details,
        people // required_people,
        cars // required_cars,
        trees // required_trees,
    )
    print(max_sets)


print(">>> Constructor(144, 8, 4, 14)")
Constructor(144, 8, 4, 14)
print(">>> Constructor(10000, 16, 6, 2)")
Constructor(10000, 16, 6, 2)


# 7
def custom_filter(data_list):
    """Фильтрует целые числа, делит на 7, суммирует и проверяет условие."""
    total_sum = 0
    for item in data_list:
        if isinstance(item, int) and not isinstance(item, bool):
            if item % 7 == 0:
                total_sum += item
    print(f">>> сумма: {total_sum}")
    print(total_sum <= 83)


print(">>> print(custom_filter([7, 10.5, 'txt', 14, 2, 56]))")
custom_filter([7, 10.5, "txt", 14, 2, 56])
print(">>> print(custom_filter([70, 21]))")
custom_filter([70, 21])


# 8
def square(x, y):
    """Выводит плоскость из чисел x, y с обрамлением."""
    top_border = "_" * (len(str(x)) + len(str(y)) + 3)
    print(top_border)
    middle = f"| {x} {y} |"
    print(middle)
    bottom_border = "¯" * (len(str(x)) + len(str(y)) + 3)
    print(bottom_border)


print(">>> square(2, 3)")
square(2, 3)
print(">>> square(100, 5000)")
square(100, 5000)
