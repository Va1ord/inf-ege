#       Вариант 8.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not(y <= x) or ((not w) == (z <= y)) or z
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       1 0 0 1
#       1 1 0 1


#       № 5
# for n in range(4, 1000):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s += s[-2:]
#     else:
#         s += s[-3:]
#     r = int(s, 2)
#     if r > 256:
#         print(n)
#         break

#       Программа выведет:
#       33


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(3):
#     fd(2 * m)
#     rt(90)
#     fd(3 * m)
#     lt(90)
# rt(180)
# fd(6 * m)
# rt(90)
# fd(9 * m)
# up()
# bk(3 * m)
# rt(90)
# down()
# for i in range(2):
#     fd(1 * m)
#     rt(90)
#     fd( 2 * m)
#     lt(90)
# rt(180)
# fd(4 * m)
# rt(90)
# fd(4 * m)
# rt(90)
# fd(1 * m)
# up()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# for x in product('123456', repeat=5):
#     s = ''.join(x)
#     if s.count('3') == 1:
#         s = s.replace('1', '3').replace('5', '3')
#         s = s.replace('4', '2').replace('6', '2')
#         if s.count('2') <= s.count('3'):
#             k += 1
# print(k)

#       Программа выведет:
#       1640


#       № 13
# from ipaddress import *
# net = ip_network('63.7.215.0/255.255.252.0', 0)
# k = 0
# for ad in net:
#     ad2 = bin(int(ad))[2:].zfill(32)
#     if ad2.count('1') % 8 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       904


#       № 14
# mx_x = 0
# for x in range(1, 801):
#     n = 7 ** 1040 + 7 ** 40 - x
#     k = 0
#     while n > 0:
#         if n % 7 == 0:
#             k += 1
#         n //= 7
#     if k == 1002:
#         mx_x = x
# print(mx_x)

#       Программа выведет:
#       784


#       № 15
# def f(x):
#     return (x % a == 0) or ((200 <= x <= 250) <= (x % 55 != 0))
#
# s = []
# for a in range(1, 300):
#     if all(f(x) == 1 for x in range(1, 300)):
#         s.append(a)
# print(max(s))

#       Программа выведет:
#       220


#       № 16
# f = {}
# for n in range(2026):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n + f[n - 1]
# print(f[2025] - f[1000])

#       Программа выведет:
#       1550825


#       № 19 - 21
# def f(x, m):
#     if x <= 34: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x - 3, m - 1), f(x - 7, m - 1), f(x // 4, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(35, 200) if f(s, 2)]))

#       Программа выведет:
#       140

# print([s for s in range(35, 200) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [143, 144, 145, 147, 148, 149]

# print(min([s for s in range(35, 200) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       146


#       № 23
# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
# print(f(2, 8) * f(8, 30))

#       Программа выведет:
#       72

