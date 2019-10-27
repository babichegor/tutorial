string = ',,,zxcv.bnma.sdfgh.jkqwe.rtyusdf,,'

#Получаем длинну строки len()
print(len(string))

#Разделяем строку split() на выходе получаем список
print(string.split('.'))

#Объединение строк join() в list_join перед точной в ковычках указывается то что будет размещено как разделитель
list1 = ['Мое','имя','забыто','предками!']
list_join = ' '.join(list1)
print(list_join)

#Метод .startswith() проверяет начинается ли строка с условия в скобках
print(string.startswith('zxc'))

#Метод .endswith() проверяет заканчивается ли строка с условия в скобках
print(string.endswith('jkc'))

#Смещение первого включения find()
print(string.find('sdf'))

#Смещение последнего включения rfind()
print(string.rfind('sdf'))

#Проверка сколько раз встречается в тексе count()
print(string.count('sdf'))

#Все символы цифры или буквы isalnum()
print(string.isalnum())

#Удаляет символы () с обеих концов strip()
print(string.strip(','))

#Первое слово с большой буквы capitalize()
string_test = 'добро пожаловать в мой мир!'
print(string_test.capitalize())

#Все слова с большой буквы title()
string_test = 'добро пожаловать в мой мир!'
print(string_test.title())

#Все слова в верхнем регистре upper() а в нижнем lower() сменить регистр swapcase()
string_test = 'добро пожаловать в мой мир!'
print(string_test.upper())

#Выравнивание строки внутри заданного количества пробелов center()
#По левому краю ljust()
#По правому краю rjust()
string_test = 'добро пожаловать в мой мир!'
print(string_test.center(40))

#Замена подстроки replace() третий аргумент количество включений которые нужно заменить
string_test = 'добро пожаловать в мой мир!'
print(string_test.replace('мой', 'ЧУЖОЙ'))