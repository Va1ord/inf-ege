#       Вариант 9.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not(x <= y) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       0 1 1 0
#       1 1 0 0


#       № 5
# def f(n):
#     s = ''
#     while n > 0:
#         s += str(n % 4)
#         n //= 4
#     return s[::-1]
#
# w = []
# for n in range(1, 100):
#     s = f(n)
#     if n % 4 == 0:
#         s += s[-2:]
#     else:
#         s = s + f((n % 4) * 2)
#     r = int(s, 4)
#     if r < 261:
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       61


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(2):
#     fd(17 * m)
#     lt(90)
#     fd(10 * m)
#     lt(90)
# up()
# bk(4 * m)
# rt(90)
# bk(3 * m)
# lt(90)
# down()
# for i in range(2):
#     fd(40 * m)
#     rt(90)
#     fd(10 * m)
#     rt(90)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 40):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# n = 0
# for x in product(sorted('ФАВОРИТ'), repeat=6):
#     s = ''.join(x)
#     k += 1
#     if s[0] != 'О' and s.count('Р') == 2:
#         if k % 2 == 0:
#             n += 1
# print(n)

#       Программа выведет:
#       8640


#       № 14
# for x in '0123456789ABCDEFGHIJKLM':
#     s1 = '1' + x + '1' + x + '1' + x + '1' + x + '1'
#     s2 = '20' + x + '24'
#     s3 = '1' + x + '235'
#     sm = int(s1, 23) + int(s2, 23) + int(s3, 23)
#     if sm % 22 == 0:
#         print(x, sm // 22)
#         break

#       Программа выведет:
#       7 4651779499


#       № 15
# def f(x, y):
#  return (4 * x + y < a) or (x < y) or (22 <= x)
#
# s = []
# for a in range(0, 200):
#     if all((f(x, y)) == 1 for x in range(0, 200) for y in range(0, 200)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       106


#       № 16
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 5
#     if n > 1:
#         f[n] = 2 * n + 1 + f[n - 1]
# print(f[2024] - f[2022])

#       Программа выведет:
#       8096


#       № 19 - 21
# def f(x, m):
#     if x >= 202: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 4, m - 1), f(x * 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 202) if f(s, 2)])

#       Программа выведет:
#       [67]

# print([s for s in range(1, 202) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [63, 66]

# print(min([s for s in range(1, 202) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       62


#       № 23
# def f(x, y):
#     if x > y or x == 11 or x == 17: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x + 4, y) + f(x * 2, y)
# print(f(3, 24))

#       Программа выведет:
#       298

