"""Сортировка пузырьком самый простой алгоритм для сортировки
какого либо массива значений сортировка идет путем сравнивания двух сосоедних чисел
если число справа больше того что слева делаем своп
если не то седующее число и так до конца
после первого прохода самое большое число будет справа
поэтому длинну массива можно уменьшить на 1"""

"""1 - создаем массив
   2 - узнать длинну массива минус 1 так как отсчет идет от индекса 0
   3 - пройти циклом от 0 до длинны массива
   4 - создаем сам цикл сортировки
   5 - он так же начинается с нуля и на каждой итерации уменьшает длинну массива т.к.
   после 1 - го прохода самое большое значение в конце массива
   6 - сравнивает значение 1 с значение 2
   7 - если разные делаем swap
"""

bubble_list = [90,52,13,67,32,74,1,16,46,71,3,4,2]

def bubble_sort(bubble_list_1):
    list_len = len(bubble_list_1) - 1
    for i in range(0, list_len):
        for x in range(0, list_len - i):
            if bubble_list_1[x] > bubble_list_1[x+1]:
                bubble_list_1[x], bubble_list_1[x+1] = bubble_list_1[x+1], bubble_list_1[x]
        print(bubble_list_1)

#bubble_sort(bubble_list)

def bubble_sort_rev(bubble_list_1):
    list_len = len(bubble_list_1) - 1
    for i in range(0, list_len):
        for x in range(0, list_len - i):
            if bubble_list_1[x+1] < bubble_list_1[x]:
                bubble_list_1[x+1], bubble_list_1[x] = bubble_list_1[x], bubble_list_1[x+1]
        print(bubble_list_1)

bubble_sort_rev(bubble_list)
