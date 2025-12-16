# 1
notebook = {}


def add_note():
    """Функция добавления новой заметки."""
    header = input("Header: ")
    text = input("Text: ")
    if header and text:
        global notebook
        notebook[header] = text
        print(f"Заметка '{header}' добавлена.")
    else:
        print("Заголовок или текст не могут быть пустыми.")


def read_notes():
    """Функция чтения заметок."""
    if not notebook:
        print("Заметок нет.")
        return
    print(", ".join(notebook.keys()))
    header = input("Which note to read? > ")
    if header in notebook:
        print(notebook[header])
    else:
        print("Такой заметки нет.")


def delete_note():
    """Функция удаления заметки."""
    if not notebook:
        print("Заметок нет.")
        return
    print(", ".join(notebook.keys()))

    header = input("Which note to delete? > ")

    if header in notebook:
        global notebook
        removed_note = notebook.pop(header)
        print(f"Note {header} removed")
    else:
        print("Такой заметки нет.")


def menu():
    """Главная функция меню для взаимодействия с пользователем."""
    while True:
        print(
            "\n[1] - Create a new note. [2] - Read all notes. [3] - Delete entry. [4] - Exit."
        )
        choice = input("> ")
        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 4.")


if __name__ == "__main__":
    menu()
