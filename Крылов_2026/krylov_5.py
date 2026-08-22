#       Вариант 5.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x <= y) and (z == (w <= x)) and (not w)
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       0 1 1 0
#       1 1 1 0


#       № 5
# for n in range(1, 100):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s = s.replace('1', '11')
#     else:
#         s = s.replace('0', '00')
#     r = int(s, 2)
#     if r > 70:
#         print(n)
#         break

#       Программа выведет:
#       14


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
# fd(5 * m)
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
# for x in product('012345', repeat=6):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('0') == 1:
#             s = s.replace('1', '3').replace('5', '3')
#             if '30' not in s and '03' not in s:
#                 k += 1
# print(k)

#       Программа выведет:
#       3250


#       № 13
# from itertools import *
# k = 0
# for x in product('01', repeat=11):
#     s = ''.join(x)
#     if (s.count('1') + 8) % 5 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       1663


#       № 14
# mx_x = 0
# for x in range(1, 5770):
#     n = 9 ** 2025 + 9 ** 1000 - x
#     k = 0
#     while n > 0:
#         if n % 9 == 0:
#             k += 1
#         n //= 9
#     if k == 1026:
#         mx_x = x
# print(mx_x)

#       Программа выведет:
#       5768


#       № 15
# def f(x):
#     return ((x % 9 == 0) <= (x % 6 != 0)) or (x + a >= 100)
#
# s = []
# for a in range(1, 300):
#     if all(f(x) == 1 for x in range(1, 300)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       82


#       № 16
# f = {}
# for n in range(2026):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n - 1]
# print(((f[2025] // 25) + f[2024]) / f[2023])

#       Программа выведет:
#       165968.0


#       № 19 - 21
# def f(x, m):
#     if x <= 31: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x - 2, m - 1), f(x - 5, m  - 1), f(x // 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(32, 100) if f(s, 2)]))

#       Программа выведет:
#       96

# print([s for s in range(32, 100) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [98, 99]

# print(min([s for s in range(32, 200) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       100


#       № 23
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 2, y) + f(x // 2, y)
# print(f(50, 11) * f(11, 2))

#       Программа выведет:
#       48

