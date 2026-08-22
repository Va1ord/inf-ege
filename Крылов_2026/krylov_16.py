#       Вариант 16.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not(w <= (not(x <= y))) and ((not x) <= ((not y) == z))
#                 if f == 0:  #  Для решения задачи необходимо проверить оба условия: при f == 0 и f == 1
#                     print(x, y, z, w)

#       Программа выведет при f == 0:
#       x y z w
#       0 0 0 0
#       0 0 0 1
#       0 0 1 0
#       0 1 0 0
#       0 1 1 0
#       0 1 1 1
#       1 0 0 0
#       1 0 0 1
#       1 0 1 0
#       1 0 1 1
#       1 1 0 0
#       1 1 1 0

#       Программа выведет при f == 1:
#       x y z w
#       0 0 1 1
#       0 1 0 1
#       1 1 0 1
#       1 1 1 1


#       № 5
# w = []
# for n in range(1, 100):
#     s = bin(n)[2:]
#     if len(s) % 2 == 0:
#         s = s[:len(s) // 2] + '1' + s[len(s) // 2:]
#     r = int(s, 2)
#     if r <= 26:
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       26


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# up()
# fd(100 * m)
# rt(90)
# fd(100 * m)
# rt(45)
# down()
# for i in range(15):
#     fd(20 * m)
#     rt(90)
#     fd(30 * m)
#     rt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# for x in product(sorted('ПОЛЬЗА'), repeat=6):
#     s = ''.join(x)
#     k += 1
#     if s.count('Ь') <= 1 and s.count('А') == 1 and s.count('З') <= 2:
#         print(k)
#         break

#       Программа выведет:
#       1599


#       № 14
# x = 1331 ** 650 - 55 * 121 ** 610 + 77 * 11 ** 510 - 3 * 11 ** 100 - 221
# k = 0
# while x > 0:
#     if x % 11 == 10:
#         k += 1
#     x //= 11
# print(k)

#       Программа выведет:
#       1236


#       № 16
# def f(n):
#     if n < 3:
#         return 1
#     if n > 2 and n % 2 != 0:
#         return f(n - 1) - f(n - 2)
#     if n > 2 and n % 2 == 0:
#         k = 0
#         for i in range(1, n):
#             k += f(i)
#         return k
#
# print(f(39))

#       Программа выведет:
#


#       № 19 - 21
# def f(x, y, m):
#     if x + y >= 123: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, y, m - 1), f(x, y + 1, m - 1), f(x * 2, y, m - 1), f(x, y * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return any(h)  #  В 21 и 22 задании поменяйте на all(h)

# print(min([s for s in range(1, 114) if f(9, s, 2)]))

#       Программа выведет:
#       29

# print([s for s in range(1, 114) if not f(9, s, 1) and f(9, s, 3)])

#       Программа выведет:
#       [52, 56]

# print(min([s for s in range(1, 114) if not f(9, s, 2) and f(9, s, 4)]))

#       Программа выведет:
#       51


#       № 23
# def f(x, y):
#     if x < y or x == 4: return 0
#     if x == y: return 1
#     return f(x - 1, y) + f(x // 2, y)
# print(f(60, 20) * f(20, 1))

#       Программа выведет:
#       1760

