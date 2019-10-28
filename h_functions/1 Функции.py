#пример простой функции
def summa_a_b(a,b): #Определение функции
    print(a + b)

summa_a_b(5,23) #Вызов функции

#Позиционые аргументы *args и *kwargs

#def func1(*args):
#    print(args)
#
#def func2(**kwargs):
#    print(kwargs)
#
#func1(1,2,3,4,5)
#func2(a ='2',b ='4',c ='6')

#Встроенные функции если втроая функиця не принимает аргументы и возвращает себя как объект func4 то это замыкание

#def func3(a,b):
#    def func4(c,d):
#        return c + d
#    return func4(a,b)
#
#a = func3(5,6)
#print(a)

#lambda - это анонимная функция

#add = lambda x,y: x**y
#print(add(2,7))
#print((lambda x,y: x+y)(5,7))

#Генераторы объект для создания последовательностей в отлиции от циклов не хранят все значения и выполняются
#последовательно при каждом обращении

#def new_range(a, b):
#    while a<b:
#        print(a)
#        yield a
#        a += 1
#
#g = new_range(1,5)
#next(g)
#next(g)
#next(g)
#next(g)

#Декораторы работают по принципу замыканий принимает на входе одну функцию в качестве аргумента
#И возвращает другую функцию
def decorator(func): #Сначала принимаем функцию
    def function(*args): #Это функция которую вернем замыкатель!
        print('Hello') 
        res = func(*args) #Вот тут принимаем функцию которую получили в самом начале!
        print('Buy') 
        return res #И возвращаем ее
    return function #Возвращаем выполненую функцию

@decorator
def func_one(name, re_name):
    print(name)
    print(re_name)

func_one('Egor', 'Babich')

#Обработка ршибок try - перехватывает исключение
# except - обработка исключения можно указать имя исключения
# else - работает когда все нормально
# finally - выполняется в любом случае

""" try:
        pass
    except NameError, IndexError, SystemExit:
        pass
    else:
        pass
    finaly:
        pass
"""