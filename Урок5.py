#Новая переменная спам умножает все значения в переменной намс на 2
nums = [1,2,3,4]
numbers2 = [spam*2 for spam in nums]
print(numbers2)

#Складывает 2 стринга и выводит суммированные значения от
my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + '2' for i in my]
print(my2[1:3])

#Вывод четных и нечетных чисел
nums = [i for i in range(1, 11)]
even = [num for num in nums if num % 2 == 0]
odd = [num for num in nums if num % 2 != 0]
print(even, odd)

#Добавляет 2 к словам с наличием буквы А
my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + '2' for i in my if 'a' in i]
print(my2)

#Вывод промежутка от 1 до 10, с шагом 2
my_list = [i for i in range(1, 11, 2)]
print(my_list)

#Вывод первых букв имен
names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
firstletters = [name[0] for name in names]
print(firstletters)

#Вычисление четных в промежутке от 1 до 20
nums1 = [num for num in range(1, 21)]
nums2 = [itog for itog in nums1 if itog % 2 == 0]
print(f'Четные числа: {nums2}')
