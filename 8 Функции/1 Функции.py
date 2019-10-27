#пример простой функции
def summa_a_b(a,b): #Определение функции
    print(a + b)

summa_a_b(5,23) #Вызов функции

#Позиционые аргументы *args и *kwargs

def func1(*args):
    print(args)

def func2(**kwargs):
    print(kwargs)

func1(1,2,3,4,5)
func2(a ='2',b ='4',c ='6')

#Встроенные функции если втроая функиця не принимает аргументы и возвращает себя как объект func4 то это замыкание

def func3(a,b):
    def func4(c,d):
        return c + d
    return func4(a,b)

a = func3(5,6)
print(a)

#lambda - это анонимная функция

add = lambda x,y: x**y
print(add(2,7))
print((lambda x,y: x+y)(5,7))