#          Тип 2 №


#  f = Логическая функция
#  Для решения таких задач есть несколько способов написания программ.

# from itertools import *  # С использованием библиотеки itertools
# print('x, y, z, w')
# for x, y, z, w in product([0, 1], repeat(4)):
#     f = (((x <= y) == (z <= w)) or (x and w))
#     if f == 0:
#         print(x, y, z, w)


    #  15097 РЕШУ ЕГЭ
# print('x y z')  # С вложенными циклами
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#                 f = (x == z) or (x <= (y and z))
#                 if f == 0:
#                     print(x, y, z)

#       Программа выведет:
#         x y z
#         1 0 0
#         1 1 0


    #  15787 РЕШУ ЕГЭ
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= y) and (y <= w)) or (z == (x or y))
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#         x y z w
#         0 1 0 0
#         1 0 0 0
#         1 0 0 1
#         1 1 0 0
