#       Вариант № 20.


#       № 2
#  (№ 5988)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = w and ((z or y) == (z and x))
#                 if f == 1:  #  Для решения задачи необходимо проверить оба условия: при f == 0 и f == 1
#                     print(x, y, z, w)

#       Программа выведет при f == 0:
#       x y z w
#       0 0 0 0
#       0 0 1 0
#       0 0 1 1
#       0 1 0 0
#       0 1 0 1
#       0 1 1 0
#       0 1 1 1
#       1 0 0 0
#       1 0 1 0
#       1 1 0 0
#       1 1 0 1
#       1 1 1 0

#       Программа выведет при f == 1:
#       x y z w
#       0 0 0 1
#       1 0 0 1
#       1 0 1 1
#       1 1 1 1


#       № 6
#  (№ 6352)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# x = 3
# lt(90)
# for i in range(2):
#     fd((3 * x) * m)
#     rt(90)
#     fd(x * m)
#     rt(90)
#     for j in range(2):
#         fd(x * m)
#         lt(90)
#     for j in range(2):
#         fd(x * m)
#         rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 12



#       № 14
#  (№ 6567)
# p = [6, 7, 8, 9]
# q = [6, 7, 8, 9]
# for i in range(4):
#     for j in range(4):
#         if int('24351', p[i]) == int('14325', q[j]):
#             print(int('24351', p[i]))

#       Программа выведет:
#       6357


#       № 19 - 21
#  (№ 5482)
# def f(x, y, m):
#     if x + y >= 231: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 2, y, m - 1), f(x, y + 2, m - 1), f(x * 2, y, m - 1), f(x, y * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return any(h)  #  В 21 и 22 задании поменяйте на all(h)

# print(max([s for s in range(1, 214) if f(17, s, 2)]))

#       Программа выведет:
#       211

# print([s for s in range(1, 214) if not f(17, s, 1) and f(17, s, 3)])

#       Программа выведет:
#       [53, 98, 104, 105]

# print(min([s for s in range(1, 214) if not f(17, s, 2) and f(17, s, 4)]))

#       Программа выведет:
#       96


#       № 23
#  (№ 6778) (ЕГЭ-2023)
# def f(x, y):
#     if x > y or x == 17: return 0
#     if x == y: return 1
#     return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)
# print(f(3, 10) * f(10, 25))

#       Программа выведет:
#       90

