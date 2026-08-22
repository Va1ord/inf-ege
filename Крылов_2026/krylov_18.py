#       Вариант 18.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((z <= y) <= x) or (not w)
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       0 1 0 1
#       0 1 1 1


#       № 5
# w = []
# for n in range(100, 1000):
#     s = str(n)
#     x1 = int(s[0]) ** 2 + int(s[1]) ** 2
#     x2 = int(s[1]) ** 2 + int(s[2]) ** 2
#     sm = str(max(x1, x2)) + str(min(x1, x2))
#     if sm == '7434':
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       753


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(10):
#     fd(7 * m)
#     rt(120)
# up()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# for x in product(sorted('ПРАВО'), repeat=4):
#     s = ''.join(x)
#     k += 1
#     if s[0] == 'П':
#         print(k)
#         break

#       Программа выведет:
#       376


#       № 14
# x = 4 ** 2022 - 2 * 4 ** 1111 + 16 ** 600 + 192
# k = 0
# while x > 0:
#     if x % 4 == 3:
#         k += 1
#     x //= 4
# print(k)

#       Программа выведет:
#       89


#       № 16
# f = {}
# for n in range(2024):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n ** 2 + f[n - 1]
# print(f[2023] - f[2019])

#       Программа выведет:
#       16345854


#       № 19 - 21
# def f(x, m):
#     if x >= 177: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 177) if f(s, 2)])

#       Программа выведет:
#       [88]

# print([s for s in range(1, 177) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [44, 87]

# print(min([s for s in range(1, 177) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       86


#       № 23
# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     return f(x + 2, y) + f(x + 7, y)
# print(f(7, 51))

#       Программа выведет:
#       639

