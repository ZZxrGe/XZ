# 1
my_dict = {1: "0101101", 2: "101110", 3: "1A14C", 4: "1100100", 5: "101010"}
print("Начальный словарь:")
print(my_dict)
if 3 in my_dict:
    del my_dict[3]
print("\nСловарь после удаления элемента с 16-ричным значением:")
print(my_dict)
my_dict[10] = "0100101"

print("\nСловарь после добавления нового элемента:")
print(my_dict)
# 2
sl = {"</>": 13, "script": 1, "__init__": 10, "self": 5, "number_9": 6, "#comment": 100}
print("Начальный словарь:")
print(sl)
try:
    user_key = input("Введите ключ для нового элемента (например, _prog): ")
    user_value = input("Введите значение для нового элемента (например, 7): ")
    sl[user_key] = user_value
except Exception as e:
    print(f"Произошла ошибка ввода: {e}")
print("\nСловарь после добавления элемента пользователем:")
print(sl)
# 3
user_dict = {}
print("Начните заполнять словарь. Ключ должен быть числом.")
while len(user_dict) < 3:
    try:
        key_input = input(f"Введите числовой ключ для элемента {len(user_dict) + 1}: ")
        key = int(key_input)
        value = input(f"Введите значение для ключа '{key}': ")
        user_dict[key] = value
        print(f"Элемент добавлен. Текущий размер словаря: {len(user_dict)}\n")
    except ValueError:
        print("Ошибка: Ключ должен быть целым числом. Попробуйте снова.\n")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}\n")
print("Словарь заполнен (достигнуто 3 элемента):")
print(user_dict)
# 4
all_d = {1: 15, 4: 80, 44: 0, 256: 15, 100: 70, 101: 70, 20: 44, 3: 9}
keys_to_remove = [1, 101, 3]
print("Начальный словарь:")
print(all_d)
for key in keys_to_remove:
    if key in all_d:
        del all_d[key]
print("\nСловарь после удаления ключей 1, 101, 3:")
print(all_d)
