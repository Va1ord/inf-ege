#       Вариант 12.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not(w <= x) or ((not z) == (not y)) or z
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 1 0 0
#       1 1 0 0
#       1 1 0 1


#       № 5
# def f(n):
#     s = ''
#     while n > 0:
#         s += str(n % 4)
#         n //= 4
#     return s[::-1]
#
# w = []
# for n in range(1, 1000):
#     s = f(n)
#     if n % 4 == 0:
#         s += s[-2:]
#     else:
#         s = s + f((n % 4) * 2)
#     r = int(s, 4)
#     if r >= 1088:
#         print(n)
#         break

#       Программа выведет:
#       68


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(3):
#     down()
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(10 * m)
#     rt(90)
# up()
# for i in range(5):
#     fd(10 * m)
#     rt(90)
#     fd(5 * m)
#     lt(90)
# up()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# n = 0
# for x in product(sorted('ИНТЕГРАЛ'), repeat=5):
#     s = ''.join(x)
#     k += 1
#     if s[0] != 'Т' and (s.count('Н') == 1 or s.count('Н') == 2):
#         if k % 2 != 0:
#             n += 1
# print(n)

#       Программа выведет:
#       5992


#       № 14
# for x in '0123456789ABCDEFGHI':
#     s1 = '3' + x + '2' + x + '1' + x + '0' + x + '1'
#     s2 = x + '2024'
#     s3 = '1' + x + '077'
#     sm = int(s1, 19) + int(s2, 19) + int(s3, 19)
#     if sm % 18 == 0:
#         print(x, sm // 18)

#       Программа выведет:
#       ...
#       G 3632718098


#       № 15
# def f(x, y):
#     return (x >= 20) or (y >= 40) or (y <= x + a) or (y >= 3 * x - a)
#
# s = []
# for a in range(0, 200):
#     if all((f(x, y)) == 1 for x in range(0, 300) for y in range(0, 200)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       19


#       № 16
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 1
#     if n == 2:
#         f[n] = 2
#     if n > 2:
#         f[n] = n * (n - 1) + f[n - 1] - f[n - 2]
# print(f[2024] + f[2020] - f[2019])

#       Программа выведет:
#       4102638


#       № 19 - 21
# def f(x, m):
#     if x >= 105: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 5, m - 1), f(x * 4, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 105) if f(s, 2)])

#       Программа выведет:
#       [26]

# print([s for s in range(1, 105) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [21, 25]

# print(min([s for s in range(1, 105) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       20


#       № 23
# def f(x, y):
#     if x > y or x == 21: return 0
#     if x == y: return 1
#     return f(x + 2, y) + f(x + 3, y) + f(x * 5, y)
# print(f(1, 6) * f(6, 35))

#       Программа выведет:
#       1692

