#Цикл с условием while
#a = 10
#while a >=1:
#    print(a)
#    a -= 1

#Прерывания цикла с помощью команды break
#while True:
#    a = int(input('Пока не напишешь 5 я буду тебя мучать!'))
#    if a == 5:
#        print('Давай счастливо!')
#        break
#    print(a)

#Пропуск шага с помощью команды continue
i = 0
for i in range(10):
    i += 1
    if i%4 == 0:
        print('Я не буду ее печатать!')
        continue
    print(i)

#Проход по нескольким с помощью zip() for a,b,c in zip(dict1,dict2,dict3) либо list(zip(a,b))