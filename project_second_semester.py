import time
from random import randint
def iteration(element):
    start = time.perf_counter()
    spisok = []
    for i in range(10):
        spisok.append(randint(1, 3))
    spisok.sort()

    central = len(spisok) // 2
    left = 0
    right = len(spisok) - 1

    while spisok[central] != element and left <= right:
        if element > spisok[central]:
            left = central + 1
        else:
            right = central - 1
        central = (left + right) // 2

    if left > right:
        print('Такого элемента нет в списке.')
    else:
        while spisok[central] == spisok[central-1]:
            central -= 1
        print('Индекс первого вхождения вашего элемента: ', central)
    stop = time.perf_counter()
    print('Время работы программы: ', stop - start, 'секунд.')

def rec(element):
    start = time.perf_counter()
    spisok = []
    spisok1 = spisok
    for i in range(10):
        spisok.append(randint(1, 3))
    spisok.sort()

    left = 0
    right = len(spisok) - 1
    def search(spisok, element):
        if len(spisok) == 0:
            return 'Такого элемента нет в списке.'
        else:
            central = len(spisok) // 2
            if spisok[central] == element:
                return central
            else:
                if element < spisok[central]:
                    return search(spisok[:central], element)
                else:
                    return  search(spisok[central+1:], element)
    return search(spisok, element)
    while spisok1[central] == spisok1[central - 1]:
        central -= 1
    stop = time.perf_counter()
    print('Время работы программы: ', stop - start, 'секунд.')

element = int(input('Введите элемент для поиска: '))
method = input('Каким методом вы хотите найти индекс вашего числа: итеративно(1) или рекурсивно?(2) ').lower().strip()
if method == '1' or method == 'итеративно':
    iteration(element)
elif method == '2' or method == 'рекурсивно':
    print('Индекс первого вхождения вашего элемента: ', rec(element))
