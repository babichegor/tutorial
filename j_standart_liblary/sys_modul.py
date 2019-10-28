#Доступ к переменным и функциям взаимодействующих с интерпритатором

import sys
print(sys.argv) #Полный путь к файлу
print(sys.executable) #Путь к интерпритатору Python
print(sys.path) #Все пути к файлу и файлам python
print(sys.platform) #Имя платформы
#print(sys.stdin.readline()) #Ввод данных на подобие input()