names = []

while True:
    new = input('Кого добавим в список контаков?: ')

    if new not in names:
        names.append(new)
        print(names)

    else:
        print(f'{new} добавлен в список контаков!')
        print('Такой пользователь уже есть в списке!')
        print(f'Весь список добавленных контаков: {names} ')


