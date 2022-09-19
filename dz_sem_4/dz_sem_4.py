
# Задача 1

# def simply_num():
#     num = int(input("Введите число: "))
#     list_num = []
#     k = 0
#     for i in range(2,num//2):
#         if num % i == 0:
#             if i % 2 !=0 and i % 5 !=0:
#                 list_num.append(i)
#             elif i==2:
#                 list_num.append(2)
#             elif i==5:
#                 list_num.append(5)
#     print(list_num)
# simply_num()

# Задача 2

# list_num  = [1,1,1,1,2,2,2,3,6,7,8,7,3,3,4]
# list_num_2 = []
# for i in list_num:
#     for j in list_num:
#         if i not in list_num_2:
#             list_num_2.append(i)
# print(list_num_2)

# Задача 3


# def write_file():
#     f = open('file.txt', 'w')
#     number_of_students = int(input('Введите кол-во студентов в группе: '))
#     for i in range(0, number_of_students):
#         Name = str(input('Введите имя и фамилию студента, через пробел: '))
#         Mark = str(input('Введите оценку студента: '))
#         if Mark == "5":
#             f.write(Name.upper())
#             f.write(" ")
#             f.write(Mark)
#             f.write('\n')
#         else:
#             f.write(Name)
#             f.write(" ")
#             f.write(Mark)
#             f.write('\n')
#     f.close
# def rede_file():
#     x = open('file.txt', 'r')
#     print(*x)
# write_file()
# rede_file()



# Задача 4

# def write_code():
#     f = open('file2.txt', 'w')
#     message = input("Сообщение для ДЕшифровки: ").upper()
#     f.write(message)
#     f.close

# def deshifrovka_1():
#     y = open('file2.txt', 'r')
#     message_read = str(y.readline())
#     y.close
#     return message_read

# def deshifrovka_2():
#     itog = ''
#     if lang == 'RU':
#         for i in deshifrovka_1():
#             mesto = alfavit_RU.find(i)
#             new_mesto = mesto + smeshenie
#             if i in alfavit_RU:
#                 itog += alfavit_RU[new_mesto]
#             else:
#                 itog += i
#     else:
#         for i in deshifrovka_1():
#             mesto = alfavit_EU.find(i)
#             new_mesto = mesto + smeshenie
#             if i in alfavit_EU:
#                 itog += alfavit_EU[new_mesto]
#             else:
#                 itog += i
#     return itog

# alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# lang = input('Выберите язык RU/EU: ')
# write_code()
# deshifrovka_1()
# smeshenie = int(input('Шаг шифровки: '))
# print (deshifrovka_2())



# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

# Задача 5



