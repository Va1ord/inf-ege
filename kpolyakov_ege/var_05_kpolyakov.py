#       Вариант № 5.


#       № 2
#  (№ 7457) (ЕГЭ-2024)
# print('x y z w')
# for x in 0,1 :
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= y) <= z) or (not w)
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       0 1 0 1
#       1 1 0 1


#       № 5
# #  (№ 7458) (ЕГЭ-2024)
# w = []
# for n in range(1, 1000):
#     s = bin(n)[2:]
#     if s.count('1') % 2 == 0:
#         s = '10' + s[2:] + '0'
#     else:
#         s = '11' + s[2:] + '1'
#     r = int(s, 2)
#     if r < 35:
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       24


#       № 6
#  	(№ 7460) (ЕГЭ-2024, Демо-2025)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 10
# lt(90)
# for i in range(9):
#     fd(22 * m)
#     rt(90)
#     fd(6 * m)
#     rt(90)
# up()
# fd(1 * m)
# rt(90)
# fd(5 * m)
# lt(90)
# down()
# for i in range(9):
#     fd(53 * m)
#     rt(90)
#     fd(75)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7464) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('012345678', repeat=6):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s[0] not in '1357' and s[-1] not in '23' and s.count('1') >= 2:
#             k += 1
# print(k)

#       Программа выведет:
#       19868


#       № 12
#  (№ 7469) (ЕГЭ-2024)
# s = 100 * '9'
# while '33333' in s or '999' in s:
#     if '33333' in s:
#         s = s.replace('33333', '99', 1)
#     else:
#         s = s.replace('999', '3', 1)
# print(s)

#       Программа выведет:
#       333


#       № 13
#  (№ 7607)
# from itertools import *
# k = 0
# for x in product('01', repeat=11):
#     s = ''.join(x)
#     if (13 + s.count('1')) % 3 == 0:
#         k += 1
# print(k)

#       Программа выведет:
#       683

#       № 14
#  (№ 7669)
# mx_x = 0  #  Максимальный x
# mx_1 = 0  #  Максимальное количество единиц
# for x in range(1, 2001):
#     n = 9 ** 250 + 9 ** 150 - x
#     k = 0
#     while n > 0:
#         if n % 9 == 1:
#             k += 1
#         n //= 9
#     if k >= mx_1:
#         mx_1 = k
#         mx_x = x
# print(mx_x)

#       Программа выведет:
#       1367


#       № 16
#  (№ 7524) (ЕГЭ-2024)
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = 2 * n * f[n - 1]
# print((f[2024] // 16 - f[2023]) // f[2022])

#       Программа выведет:
#       1019592


#       № 19 - 21
#  (№ 7490) (ЕГЭ-2024)
# def f(x, y, m):
#     if x + y >= 65: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, y, m - 1), f(x, y + 1, m - 1), f(x * 3, y, m - 1), f(x, y * 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return any(h)  #  В 21 и 22 задании поменяйте на all(h)

# print(min([s for s in range(1, 58) if f(6, s, 2)]))

#       Программа выведет:
#       7

# print([s for s in range(1, 58) if not f(6, s, 1) and f(6, s, 3)])

#       Программа выведет:
#       [10, 19]

# print(min([s for s in range(1, 58) if not f(6, s, 2) and f(6, s, 4)]))

#       Программа выведет:
#       18


#       № 23
#  (№ 7493) (ЕГЭ-2024)
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 1, y) + f(x // 2, y)
# print(f(30, 8) * f(8, 1))

#       Программа выведет:
#       288

