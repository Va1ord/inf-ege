#       Вариант 20.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= y) <= w) or (z <= (y and w))
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       0 1 1 0
#       1 1 1 0


#       № 5
# w = []
# for n in range(100, 1000):
#     s = str(n)
#     x1 = int(s[0]) * int(s[1]) * int(s[2])
#     x2 = int(s[0]) + int(s[1]) + int(s[2])
#     sm = str(max(x1, x2)) + str(min(x1, x2))
#     if sm == '24019':
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       865


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 10
# lt(90)
# for i in range(18):
#     fd(19 * m)
#     rt(60)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# for x in product(sorted('ВАЛИК'), repeat=6):
#     s = ''.join(x)
#     k += 1
#     if s.count('А') <= 2 and s.count('В') == 2 and 'И' not in s:
#         print(k)
#         break

#       Программа выведет:
#       169


#       № 14
# x = 3 ** 2021 + 5 * 3 ** 2000 + 3 ** 501 + 5 * 3 ** 500 + 1
# k = 0
# while x > 0:
#     if x % 9 == 0:
#         k += 1
#     x //= 9
# print(k)

#       Программа выведет:
#       1007


#       № 16
# f = {}
# for n in range(2024):
#     if n == 1:
#         f[n] = 1
#     if n == 2:
#         f[n] = 2
#     if n > 2:
#         f[n] = n * (n - 1) + f[n - 1] + f[n - 2]
# print(f[2023] - f[2021] - 2 * f[2020] - f[2019])

#       Программа выведет:
#       12259388


#       № 19 - 21
# def f(x, m):
#     if x >= 2022: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 2021) if f(s, 2)])

#       Программа выведет:
#       [1010]

# print([s for s in range(1, 2021) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [505, 1009]

# print(min([s for s in range(1, 2021) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       1008


#       № 23
# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     return f(x + 2, y) + f(x + 10, y)
# print(f(7, 71))

#       Программа выведет:
#       4085

