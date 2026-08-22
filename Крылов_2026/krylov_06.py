#       Вариант 6.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (y <= z) and (w == (x <= y)) and (not x)
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       0 0 1 1
#       0 1 1 1


#       № 5
# for n in range(1, 100):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s = s.replace('1', '11')
#     else:
#         s = s.replace('0', '00')
#     r = int(s, 2)
#     if r < 70:
#         print(r, n)

#       Программа выведет:
#       1 1
#       6 2
#       3 3 ...
#       57 29 - Ответ
#       31 31
#       63 63


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(5):
#     fd(30 * m)
#     rt(90)
#     fd(40 * m)
#     rt(90)
# up()
# fd(20 * m)
# rt(90)
# fd(15 * m)
# rt(90)
# down()
# for i in range(7):
#     fd(10 * m)
#     rt(90)
# up()
# for x in range(-10, 50):
#     for y in range(-20, 40):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# for x in product('0123456', repeat=6):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('0') == 1:
#             s = s.replace('4', '2').replace('6', '2')
#             if '20' not in s and '02' not in s:
#                 k += 1
# print(k)

#       Программа выведет:
#       11664


#       № 13
# from ipaddress import *
# net = ip_network('200.33.100.0/255.255.248.0', 0)
# k = 0
# for ad in net:
#     ad2 = bin(int(ad))[2:].zfill(32)
#     if ad2.count('1') % 7 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       1717


#       № 14
# mx_x = 0
# for x in range(1, 2736):
#     n = 5 ** 2025 + 5 ** 1500 - x
#     k = 0
#     while n > 0:
#         if n % 5 == 0:
#             k += 1
#         n //= 5
#     if k == 527:
#         mx_x = x
# print(mx_x)

#       Программа выведет:
#       2734


#       № 15
# def f(x):
#     return ((x % 14 == 0) <= (x % 4 != 0)) or (x + a >= 200)
#
# s = []
# for a in range(1, 300):
#     if all(f(x) == 1 for x in range(1, 300)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       172


#       № 16
# f = {}
# for n in range(3001):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n - 1]
# print(((f[3000] // 150) + f[2999]) / f[2998])

#       Программа выведет:
#       62979.0


#       № 19 - 21
# def f(x, m):
#     if x <= 49: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x - 2, m - 1), f(x - 5, m  - 1), f(x // 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(50, 200) if f(s, 2)]))

#       Программа выведет:
#       150

# print([s for s in range(50, 200) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [152, 153, 155, 156]

# print(min([s for s in range(50, 200) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       154


#       № 23
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 2, y) + f(x // 2, y)
# print(f(52, 14) * f(14, 2))

#       Программа выведет:
#       64

