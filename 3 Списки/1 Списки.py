#Списки создаются в [] это пустой список либо с помощью функции list()
list1 = []
new_list = list()

#В список можно преобразовать строку list()
new_str = 'Hello'
print(list(new_str))
print(list('Hello'))

#Можно кортеж
new_str_tuple = ('Hello', 'my', 'World')
print(list(new_str_tuple))

#Спискам также доступны индексы []
new_str_index = ['Hello', 'my', 'World']
print(new_str_index[0])

#Списки могут хранить списки =) индексы работают почти также тока [][]
list_dog = ['dog1', 'dog2', 'dog3']
list_cat = ['cat1', 'cat2', 'cat3']
list_animals = [list_dog, list_cat]
print(list_animals)