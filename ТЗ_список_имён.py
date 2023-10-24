usernames = []

while True:

    username = input("Введите имя: ")

    if username in usernames:
        print("Такое имя уже существует. Попробуйте другое имя.")
    else:
        usernames.append(username)
        print("Имя успешно добавлено.")
        print(f'Весь список добавленных имён: {usernames} ')
