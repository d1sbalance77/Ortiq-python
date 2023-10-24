#Первый пример: Создание списка чисел от 1 до 10

# numbers = [num for num in range(1, 11)]
# print(numbers)

#Второй примеp: Умножает все числа на два от 1 до 11

# numbers = [num**2 for num in range(1, 11)]
# print(numbers)

#Третий примеp: Создание списка только четных чисел от 1 до 10

# even_numbers = [num for num in range(1, 11) if num % 2 == 0]
# print(even_numbers)

#Четвертый пример: Вывод четных и нечетных чисел

# nums = [i for i in range(1, 11)]
# even = [num for num in nums if num % 2 == 0]
# odd = [num for num in nums if num % 2 != 0]
# print(even, odd)

#Пятый пример: Добавляет 2 к словам с наличием буквы А

# my = ['2', '33', 'Jordan', 'Pavel']
# my2 = [i + '2' for i in my if 'a' in i]
# print(my2)

#Шестой пример: Вывод первых букв имен

# names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
# first_letters = [name[0] for name in names]
# print(first_letters)

#Седьмой пример: Добовление 2 в индекс

# my = ['2', '33', 'Jordan', 'Pavel']
# my2 = [i + '2' for i in my]
# print(my2[1:3])
