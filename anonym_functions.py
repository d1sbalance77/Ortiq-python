numbers = []
while True:

    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    sum_numbers = lambda x ,y: x + y
    result = sum_numbers(x, y)
    print(f'Сумма чисел {x} и {y}: {result}')
