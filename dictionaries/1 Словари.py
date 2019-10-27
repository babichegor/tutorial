#Словари создаются через фигурные скобки {} имеют ключ и значени
dict1 = {'ключ':'Значение увидим это в консоли!',
    'ключ1':'Значение1',
    'ключ2':'Значение2',
    'ключ3':'Значение3',    
    }

print(dict1['ключ'])

#Словарь можно создать из списков и кортежей 
new1 = [('1','2'), ('3','4')]
new2 = (['5','6'], ['7','8'])
new3 = ['12', '34', '56']
new4 = ('65','43','21')
print(dict(new1))
print(dict(new2))
print(dict(new3))
print(dict(new4))

#Удалелин элемента по его ключу del
del dict1['ключ1']
print(dict1)

#Удаление всех элементов с помощью clear()
dict3 = {'ключ':'Значение увидим это в консоли!',
    'ключ1':'Значение1',
    'ключ2':'Значение2',
    'ключ3':'Значение3',    
    }
print(dict3.clear())

#Проверка наличия ключа с помощью in
print('ключ2' in dict1)

#Получение элемента с помощью ['ключ'] с помощью dict.get('ключ23') если такого ключа нет получим ответ
print(dict1['ключ3'])

#Получение всех ключей с помощью keys() с помощью values() все значения
print(dict1.keys())
print(dict1.values())

#Все пары ключ:значение items()
print(dict1.items())

#Присваивание нового значения в словарь через = и скопировать ключи и значения dict.copy()
dict1['ключ5'] = 'Тут новое значение'
print(dict1)