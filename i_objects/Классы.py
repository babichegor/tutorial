#Классы в Python используется для описания какой либо структуры

class First_class():
    def __init__(self, names, ages, genders): #__init__ инизиализация объект с помощью определения его класса
        self.name = names #self. это указатель на объект
        self.age = ages
        self.gender = genders
        #print(names + ages + ' ' + genders + ' Первое') #Обращение к аргументам на прямую
        #print(self.age + ' ' + self.name + ' Как то так!') #Обращение к аргументам через self

    def first_func(self):
        return self.age + ' ' + self.name


a = First_class('Egors', ' 29', 'men')
print(a.name + ' - Ссылаемся через точку') #Вот тут и используется .self мы ссылаемся на атрибут класса
print(a.first_func()) #Вызов определенной функции класса

#Метод super().__init__(имя родительского аргумента)

class Two_class(First_class):
    def __init__(self, names, ages, genders, prof):
        super().__init__(names, ages, genders)
        self.prof = prof
        print(self.name + ' ' + self.prof + ' ' + self.gender + ' ' + self.age)

Two_class('Egors', ' 29', 'men','Developer')