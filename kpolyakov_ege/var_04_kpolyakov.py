#       Вариант № 4.


#       № 2
#  (№ 7511) (ЕГЭ-2024)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (y <= (not(x <= x))) or w
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 1 0 0
#       0 1 1 0
#       1 1 0 0
#       1 1 1 0


#       № 5
#  (№ 7514) (ЕГЭ-2024)
# w = []
# for n in range(1, 13):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s += '10'
#     else:
#         s = '1' + s + '01'
#     r = int(s, 2)
#     w.append(r)
# print(max(w))

#       Программа выведет:
#       109


#       № 6
#  	(№ 7515) (ЕГЭ-2024)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 10
# lt(90)
# for i in range(3):
#     fd(7 * m)
#     rt(90)
#     fd(12 * m)
#     rt(90)
# up()
# fd(4 * m)
# rt(90)
# fd(6 * m)
# lt(90)
# down()
# for i in range(4):
#     fd(83 * m)
#     rt(90)
#     fd(77 * m)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7517) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product(sorted('ФОКУС'), repeat=5):
#     s = ''.join(x)
#     k += 1
#     if s.count('Ф') == 0 and s.count('У') == 2:
#         last = k
# print(last)

#       Программа выведет:
#       2313


#       № 12
#  	(№ 7470) (ЕГЭ-2024
# s = 108 * '7'
# while '33333' in s or '777' in s:
#     if '33333' in s:
#         s = s.replace('33333', '7', 1)
#     else:
#         s = s.replace('777', '3', 1)
# print(s)

#       Программа выведет:
#       3337


#       № 13
#  (№ 7608)
# from itertools import *
# k = 0
# for x in product('01', repeat=10):
#     s = ''.join(x)
#     if (11 + s.count('1')) % 7 == 0:
#         k += 1
# print(k)

#       Программа выведет:
#       121


#       № 14
#  (№ 7670)
# for x in range(10000, 1, -1):
#     n = 6 ** 900 + 6 ** 10 - x
#     t = 0
#     s = 0
#     while n > 0:
#         if n % 6 == 3:
#             t += 1
#         if n % 6 == 5:
#             s += 1
#         n //= 6
#     if t == s:
#         print(x)
#         break

#       Программа выведет:
#       9591


#       № 15
#  (№ 7481)
# def f(x):
#     return ((x % 2 == 0) <= (x % 5 != 0)) or (x + a >= 70)
# s = []
# for a in range(1, 300):
#     if all(f(x) == 1 for x in range(1, 300)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       60


#       № 16
#  (№ 7561) (ЕГЭ-2024)
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = (n + 1) * f[n - 1]
# print((f[2024] - 3 * f[2023]) // f[2022])

#       Программа выведет:
#       4092528


#       № 17
#  (№ 7683)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17.txt')
# s = [int(s) for s in f]
# # print(s)  #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# mn = []
# mx = []
# for i in range(len(s)):
#     if s[i] % 3 == 0:
#         mn.append(s[i])
#     if s[i] % 10 == 3:
#         mx.append(s[i])
# for i in range(len(s) - 1):
#     if ((min(mn) <= s[i] <= max(mx)) and (s[i + 1] < min(mn) or s[i + 1] > max(mx))):
#         k += 1
#         w.append(s[i] ** 2 + s[i + 1] ** 2)
# print(k, min(w))

#       Программа выведет:
#       24 10309


#       № 19 - 21
#  (№ 7528) (ЕГЭ-2024)
# def f(x, m):
#     if x >= 58: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 4, m - 1), f(x * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(1, 57) if f(s, 2)]))

#       Программа выведет:
#       28

# print([s for s in range(1, 57) if not f(s, 1) and f(s ,3)])

#       Программа выведет:
#       [14, 24, 27]

# print(min([s for s in range(1, 57) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       23


#       № 23
#  (№ 7530) (ЕГЭ-2024)
# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)
# print(f(5, 7) * f(7, 11))

#       Программа выведет:
#       14

