#       Вариант № 8.


#       № 2
#  (№ 6806)
# print('x y z w')
# for x in 0,1 :
#     for y in 0,1 :
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (w or x or y) <= ((y or z) and x or y and (w or z))
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       0 0 1 1
#       0 1 0 0
#       1 0 0 0
#       1 0 0 1


#       № 5
#  (№ 7406)
# def f(n):
#     alf = '0123456789AB'
#     s = ''
#     while n > 0:
#         s += alf[n % 12]
#         n //= 12
#     return s[::-1]
#
# w = []
# mx_r, mx_n = 0, 0
# for n in range(144, 1000):
#     s = f(n)
#     if n % 12 == 0:
#         s += s[-3:]
#     else:
#         s = f((n % 12) * 3) + s
#     r = int(s, 12)
#     if mx_r < r < 58000:
#         mx_r = r
#         mx_n = n
# print(mx_n, mx_r)

#       Программа выведет:
#       971 57995


#       № 6
#  (№ 7361)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 10
# lt(90)
# up()
# for i in range(10):
#     rt(120)
#     fd(10 * m)
# down()
# for i in range(7):
#     fd(15 * m)
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
#  (№ 7411)
# from itertools import *
# k = 0
# for x in product('012345678', repeat=7):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s[0] not in '1357' and s[-1] in '124578':
#             if s.count('6') >= 1:
#                 k += 1
# print(k)

#       Программа выведет:
#       827352


#       № 12
#  	(№ 6736)
# for n in range(101, 1000):
#     s = n * '5'
#     while '555' in s or '11' in s or '2' in s:
#         if '555' in s:
#             s = s.replace('555', '1', 1)
#         if '11' in s:
#             s = s.replace('11', '25', 1)
#         if '2' in s:
#             s = s.replace('2', '5', 1)
#     if s == '15':
#         print(n)
#         break

#       Программа выведет:
#       104


#       № 13
#  (№ 7522) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('01', repeat=20):
#     s = ''.join(x)
#     if (5 + s.count('1')) % 3 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       699050


#       № 14
#  (№ 7629) (Демо-2025)
# w = []
# for x in range(1, 2030):
#     n = 7 ** 170 + 7 ** 100 - x
#     k = 0
#     while n > 0:
#         if n % 7 == 0:
#             k += 1
#         n //= 7
#     if k == 71:
#         w.append(x)
# print(max(w))

#       Программа выведет:
#       2029


#       № 15
#  (№ 7262)
# for a in range(1, 33000):
#     if all((((x & 32765 != 0) or (x & 22635 != 0)) <= (x & a > 0) for x in range(1, 33000))):
#         print(a)

#       Программа выведет:
#       32767


#       № 16
#  	(№ 7482) (ЕГЭ-2024)
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = 2 * n * f[n - 1]
# print((f[2024] - 4 * f[2023]) // f[2022])

#       Программа выведет:
#       16362024


#       № 19 - 21
#  (№ 7380)
# def f(x, m):
#     if 20 <= x <= 26: return m % 2 == 0
#     if x > 26: return m % 2 != 0
#     if m == 0: return 0
#     h = [f(x + 4, m - 1), f(x * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(1, 20) if f(s, 2)]))

#       Программа выведет:
#       6

# print([s for s in range(1, 20) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [2, 3, 4, 5, 7]

# print(len([s for s in range(1, 20) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       1


#       № 23
#  (№ 7224)
# def f(x, y, k):
#     if x > y: return 0
#     if x == y: return 1
#     else:
#         if k == 'C':
#             return f(x + 3, y, 'B') + f(x * 4, y, 'C')
#         else:
#             return f(x + 2, y, 'A') + f(x + 3, y, 'B') + f(x * 4, y, 'C')
# print(f(1, 50, ''))

#       Программа выведет:
#       484575

