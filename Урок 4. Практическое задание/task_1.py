"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from timeit import timeit

'''Задача 1. Проверка равенства: 1+2+...+n = n(n+1)/2 для множества натуральных чисел.'''

print(timeit('''
number_n = int(input('Введите любое натуральное число для n: '))
right_part = number_n * (number_n + 1) / 2
left_part = 0
while left_part != right_part:
    left_part += 1
    if left_part == right_part:
        print(f'Равенство для {number_n} выполняется!')
''', number=1))


def equality(n: int, right_part=0, left_part=1):
    if right_part == left_part:
        return 'Равенство для выполняется!'
    elif right_part < left_part:
        return equality(n, right_part + 1, n * (n + 1) // 2)


try:
    number_n = int(input('Введите любое натуральное число для n: '))
    equality(number_n)
except ValueError:
    print('Введены некорректные данные!')

print('Реализация через рекурсию')
print(timeit('equality', setup='from __main__ import equality', number=1))

'''
При реализации задачи через простой цикл время выполнения алгоритма для
числа 10 составляет 2.34 сек, сложность этого алгоритма - О(n). Если
оптимизировать этот алгоритм, переписав его в виде функции, через рекурсию, 
то время выполнения уменьшается в 1 000 000 раз до 9*10-6 сек. 
Сложность остается алгоритма также линейной.
'''

'''
Задача 2. Определить, какое число в массиве встречается чаще всего
'''

# Реализация через цикл
print(timeit('''
my_list = [random.randint(1, 100) for i in range(20)]
num = my_list[0]
max_frq = 1
for i in range(len(my_list) - 1):
    frq = 1
    for k in range(i + 1, len(my_list)):
        if my_list[i] == my_list[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = my_list[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
''', 'import random', number=1000))

# реализация через встроенную функцию
print(timeit('''
my_list = [random.randint(1, 100) for i in range(20)]
print(f'В массиве: {my_list} Чаще всего встречается: {max(my_list, key=my_list.count)}')
''', 'import random', number=1000))

'''
При реализации задачи через цикл время выполнения алгоритма для
массива из 20 чисел составляет 1.234 сек, сложность этого алгоритма - О(n^2). Если
оптимизировать этот алгоритм, используя встроенную функцию max c ключом count, 
то время выполнения остается примерно одинаковым 1.413 сек. 
Сложность алгоритма становится линейной. Но во втором случае код компактнее.
'''
