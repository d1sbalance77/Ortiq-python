def add_client(clients_dict):
    name = input("Введите имя студента: ")
    room_number = input("Введите класс от 1-11: ")
    clients_dict[name] = room_number

def remove_client(clients_dict):
    name = input("Введите имя студента для удаления: ")
    if name in clients_dict:
        clients_dict.pop(name)
        print("Студент успешно удален.")
    else:
        print("Студент с таким именем не найден.")

def show_occupied_rooms(clients_dict):
    print("Информация о студенте:")
    for name, room_number in clients_dict.items():
        print(f"{name}: {room_number}")

def main_body():
    clients = {}
    while True:
        print("Выберите действие:")
        print("1. Добавить Студента")
        print("2. Удалить Студента")
        print("3. Увидеть в каком классе учиться студент")
        print("4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            add_client(clients)
        elif choice == "2":
            remove_client(clients)
        elif choice == "3":
            show_occupied_rooms(clients)
        elif choice == "4":
            break
        else:
            print("Некорректный ввод. Повторите попытку.")


main_body()


