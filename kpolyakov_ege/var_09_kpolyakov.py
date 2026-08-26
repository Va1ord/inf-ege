#       Вариант № 9.


#       № 2
#  	(№ 6805) (ЕГЭ-2023)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x <= (z == w)) or (not (y <= w))
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       1 0 0 1
#       1 0 1 0
#       1 1 0 1


#       № 5
#  (№ 7405)
# def f(n):
#     w = []
#     while n > 0:
#         w.append(n % 13)
#         n //= 13
#     return w[::-1]
#
# r = 0
# for n in range(34, 35):
#     w = f(n)
#     # print(w)
#     for i in range(2):
#         m = f(sum(w) % 13)
#         # print(m)
#         w.append(m[0])
#         # print(w)
#     w = w[::-1]
#     for i in range(len(w)):
#         r += w[i] * 13 ** i
#     if r < 6000:
#         print(n, r)

#       Программа выведет:
#       34 5883


#       № 6
#  (№ 7360)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# up()
# for i in range(10):
#     rt(120)
#     fd(12 * m)
# down()
# for i in range(7):
#     fd(7 * m)
#     rt(90)
# for i in range(5):
#     rt(60)
#     fd(20 * m)
#     rt(30)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7398)
# from itertools import *
# k = 0
# w = []
# for x in product('АВР', repeat=7):
#     s = ''.join(x)
#     if s.count('А') == 3 and s.count('В') == 2 and s.count('Р') == 2:
#         k += 1
#         if s[0] == 'В' and 'ААА' in s and 'РР' not in s:
#             if k % 2 == 0:
#                 w.append(k)
# print(max(w))

#       Программа выведет:
#       146


#       № 12
#  (№ 6735) (ЕГЭ-2023)
# for n in range(3, 1000):
#     s = '5' + n * '2'
#     while '72' in s or '522' in s or '2222' in s:
#         if '72' in s:
#             s = s.replace('72', '2', 1)
#         if '522' in s:
#             s = s.replace('522', '27', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#     if sum([int(i) for i in s]) == 63:
#         print(n)
#         break

#       Программа выведет:
#       186


#       № 13
#  (№ 7472) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('01', repeat=14):
#     s = ''.join(x)
#     if (6 + s.count('1')) % 2 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       8192


#       № 14
#  (№ 7558) (ЕГЭ-2024)
# mx_x = 0  #  Максимальный x
# mx_0 = 0  #  Максимальное количество нулей
# for x in range(1, 2031):
#     n = 6 ** 2030 + 6 ** 100 - x
#     k = 0
#     while n > 0:
#         if n % 6 == 0:
#             k += 1
#         n //= 6
#     if k > mx_0:
#         mx_0 = k
#         mx_x = x
# print(mx_0)

#       Программа выведет:
#       1934


#       № 15
#  (№ 7261)
# for a in range(1, 120000):
#     if all(((x & 84653 != 0) or (x & 51763 != 0)) <= (x & a > 0) for x in range(1, 120000)):
#         print(a)
#         break

#       Программа выведет:
#       117439


#       № 16
#  (№ 7426)
# f = {}
# for n in range(3016):
#     if n < 7:
#         f[n] = 7
#     if n >= 7 and n % 3 != 0:
#         f[n] = 5 - f[n - 1]
#     if n >= 7 and n % 3 == 0:
#         f[n] = 3 + f[n - 1]
# print(f[3015])

#       Программа выведет:
#       3016


#       № 19 - 21
#  	(№ 6833)
# def f(x, m):
#     if x >= 37: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 2, m - 1), f(x * 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(1, 37) if f(s, 2)]))

#       Программа выведет:
#       12

# print([s for s in range(1, 37) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [4, 10, 11]

# print([s for s in range(1, 37) if not f(s, 2) and f(s, 4)])

#       Программа выведет:
#       [9]


#       № 23
#  (№ 7213)
#  Видеоразбор https://rutube.ru/video/017d703d4d9c41a11eeb86e4038c3754/
# from functools import *
#
#
# @cache
def f(x, y, k, p):
    if x == y: return p
    if x > y + 5 or x % 10 == 3:
        return 0
    else:
        z = 0
        if x == 60:
            p = 1
        z = f(x + 7, y, 3, p) + f(x * 2, y, 4, p)
        if k != 1:
            z += f(x - 1, y, 1, p) + f(x - 5, y, 1, p)
        return z
print(f(9, 84, 0, 0))

#       Программа выведет:
#       1559549

