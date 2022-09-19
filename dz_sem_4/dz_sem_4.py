
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
