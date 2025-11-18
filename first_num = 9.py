# 1  задание
second_num = 7.8
my_str = "start"

print(first_num)
print(second_num)
print(my_str)

first_num = 5.2

print(first_num)
print(type(first_num))

third_num = first_num + second_num
print(third_num)
print(type(third_num))

first_num += 5
second_num += first_num

print(second_num)

second_num = int(second_num)

print(first_num)
print(second_num)

my_str += "stop"

print(my_str)

my_str *= 5

print(my_str)


# 2 задание

path = "C:\\Users\\MainAdmin\\Desktop\\programs"
print(path)
path += "\\game.exe"
print(path)
path = "C:\\Users\\MainAdmin\\Desktop\\files"
path += "\\picture.png"
print(path)
path = "C:\\Games\\city simulator"
print(path)
path *= 2
print("Error path:", path)
