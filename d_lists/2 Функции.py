#Добавление элемента в конец списка append()
list_test = ['1', '2']
list_test.append('3')
print(list_test)

#Списки можно объединять extend() или использовать +=
list_test1 = ['4', '5', '6']
list_test.extend(list_test1)
print(list_test)

#Добавление в определенное место .insert(3, 'Текст') первый аргумент это индекс второй что разместить

#Функция del list_test[1] удаляет элемент по индексу

#Удаление по имени remove()
list_test.remove('2')
print(list_test)

#Функция pop() получает элемент по индексу если не указан то последний удаляет его из списка

#Функция index() можно узнать смещение элемента по его имени
print(list_test.index('5'))

#Проверка на вхождение in
print('4' in list_test)

#Узнать сколько раз попадается в списке count()
print(list_test.count('2'))

#Сортировка списка sort() сортирует сам списко sorted() возвращает отсортированную копию
#можно передfть аргумент (reverse=True)
list_test2 = ['d','a','f','c','b']
print(sorted(list_test2))

list_test3 = ['d','x','f','c','b','z']
list_test3.sort()
print(list_test3)

#Копия списка copy()
abc = list_test.copy()
print(abc)