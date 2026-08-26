#       Вариант № 1.


#       № 2
#  (№ 7642) (Демо-2025)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((w <= y) <= x) or (not z)
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       0 1 1 0
#       0 1 1 1


#       № 5
#  (№ 7639) (Демо-2025)
# w = []
# for n in range(1, 13):
#     s = bin(n)[2:]
#     if s.count('1') % 2 == 0:
#         s = '10' + s
#     else:
#         s = '1' + s + '01'
#     r = int(s, 2)
#     w.append(r)
# print(max(w))

#       Программа выведет:
#       109


#       № 6
#  (№ 7638)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(9):
#     fd(12 * m)
#     rt(90)
#     fd(6 * m)
#     rt(90)
# up()
# fd(1 * m)
# rt(90)
# fd(3 * m)
# lt(90)
# down()
# for i in range(9):
#     fd(53 * m)
#     rt(90)
#     fd(75 * m)
#     rt(90)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7636) (Демо-2025)
# from itertools import *
# k = 0
# for x in product('0123456789AB', repeat=5):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('7') == 1:
#             s = s.replace('9', 'A').replace('B', 'A')
#             if s.count('A') <= 3:
#                 k += 1
# print(k)

#       Программа выведет:
#       67476


#       № 12
#  (№ 7554) (ЕГЭ-2024)
# s = '9' * 81
# while '33333' in s or '999' in s:
#     if '33333' in s:
#         s = s.replace('33333', '99', 1)
#     else:
#         s = s.replace('999', '3', 1)
# print(s)

#       Программа выведет:
#       3


#       № 13
#  (№ 7632) (Демо-2025)
# from itertools import *
# k = 0
# for x in product('01', repeat=11):
#     s = ''.join(x)
#     if (8 + s.count('1')) % 5 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       1663


#       № 14
#  (№ 7673)
# for x in range(50000, 60000):
#     n = 3 ** 2000 + 3 ** 10 - x
#     k = 0
#     while n > 0:
#         if n % 3 == 2:
#             k += 1
#         n //= 3
#     if k == 2000:
#         print(x)
#         break

#       Программа выведет:
#       59050


#       № 15
#  (№ 7560) (ЕГЭ-2024)
# def f(x, y):
#     return (x + y <= 30) or (y <= x + 2) or (y >= a)
# s = []
# for a in range(0, 300):
#     if all(f(x, y) == 1 for x in range(0, 300) for y in range(0, 300)):
#         s.append(a)
# print(max(s))

#       Программа выведет:
#       17


#       № 16
#  (№ 7628) (Демо-2025)
# f = {}
# for n in range(1, 2025):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = (n - 1) * f[n - 1]
# print((f[2024] + 2 * f[2023]) // f[2022])

#       Программа выведет:
#       4094550


#       № 17
#  (№ 7718)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17.txt')
# s = [int(x) for x in f]
# # print(s)   #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s)):
#     if s[i] % 10 == 3:
#         w.append(s[i])
# mx = max(w)
# for i in range(len(s) - 3):
#     k2 = 0
#     if s[i] < mx and s[i + 1] < mx and s[i + 2] < mx and s[i + 3] < mx:
#         if s[i] % 10 == 2:
#             k2 += 1
#         if s[i + 1] % 10 == 2:
#             k2 += 1
#         if s[i + 2] % 10 == 2:
#             k2 += 1
#         if s[i + 3] % 10 == 2:
#             k2 += 1
#         if k2 % 2 != 0:
#             k += 1
#             m.append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
# print(k, min(m))

#       Программа выведет:
#       49 715


#       № 19 - 21
#  (№ 7625) (Демо-2025)
# def f(x, m):
#     if x <= 19: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x - 2, m - 1), f(x - 5, m - 1), f(x // 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(20, 100) if f(s, 2)]))

#       Программа выведет:
#       60

# print([s for s in range(20, 100) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [62, 63, 65, 66]

# print(min([s for s in range(20, 100) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       64


#       № 23
#  (№ 7574) (ЕГЭ-2024)
# def f(x, y):
#     if y > x: return 0
#     if x == y: return 1
#     return f(x - 2, y) + f(x // 2, y)
# print(f(38, 16) * f(16, 2))

#       Программа выведет:
#       36

