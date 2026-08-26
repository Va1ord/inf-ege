#       Вариант № 7.


#       № 2
#  	(№ 7415)
# print('a b c d')
# for a in 0, 1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 f = (a <= b) and (b <= (not c)) and ((not c) <= d)
#                 if f == 1:
#                     print(a, b, c, d)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       0 0 1 0
#       0 0 1 1
#       0 1 0 1
#       1 1 0 1


#       № 5
#  	(№ 7407)
# def f(n):
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
#
# w = []
# for n in range(1, 10000):
#     s = f(n)
#     if n % 2 == 0:
#         s = '2' + s + f(2 * int(s[-1]))
#     else:
#         s = f(2 * int(s[0])) + s + '2'
#     r = int(s, 3)
#     if r > 100:
#         w.append(r)
# print(min(w))

#       Программа выведет:
#       131


#       № 6
#  	(№ 7410)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# rt(45)
# for i in range(10):
#     rt(45)
#     fd(203 * m)
#     rt(45)
# up()
# bk(40 * m)
# rt(45)
# down()
# for i in range(5):
#     fd(20 * m)
#     lt(90)
# up()
# for x in range(-203, 250):
#     for y in range(-203, 170):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7462) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('012345678', repeat=5):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('0') == 1:
#             s = s.replace('3', '1').replace('5', '1').replace('7', '1')
#             if '01' not in s and '10' not in s:
#                 k += 1
# print(k)

#       Программа выведет:
#       5120


#       № 12
#  (№ 6737)
# for n in range(1, 1000):
#     s = '1' + n * '7'
#     while '17' in s or '377' in s or '777' in s:
#         if '17' in s:
#             s = s.replace('17', '1', 1)
#         if '377' in s:
#             s = s.replace('377', '73', 1)
#         if '777' in s:
#             s = s.replace('777' ,'3', 1)
#     if s.count('3') == 2:
#         print(n)
#         break

#       Программа выведет:
#       9


#       № 13
#  	(№ 7555) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('01', repeat=20):
#     s = ''.join(x)
#     if (5 + s.count('1')) % 5 == 0:
#         k += 1
# print(k)

#       Программа выведет:
#       215766


#       № 14
#  (№ 7631) (Демо-2025)
# for x in '0123456789ABCDEFGHI':
#      n1 = '98897' + x + '21'
#      n2 = '2' + x + '923'
#      f = int(n1, 19) + int(n2, 19)
#      if f % 18 == 0:
#          print(x, f // 18)

#       Программа выведет:
#       6 469030538
#       F 469034148 - Ответ


#       № 16
#  	(№ 7483) (ЕГЭ-2024)
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n - 1]
# print((2 * f[2024] + f[2023]) // f[2022])

#       Программа выведет:
#       8191127


#       № 17
#  (№ 7627) (Демо-2025)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17.txt')
# s = [int(x) for x in f]
# # print(s)   #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s)):
#     m.append(s[i])
# mn = min(m)
# for i in range(len(s) - 1):
#     if s[i] % 16 == mn or s[i + 1] % 16 == mn:
#         k += 1
#         w.append(s[i] + s[i + 1])
# print(k, max(w))

#       Программа выведет:
#       1214 176024


#       № 19 - 21
#  (№ 7381)
# def f(x, m):
#     if x == 0: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x - 2, m - 1), f(x - 3, m - 1), f(x // 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(len([s for s in range(1, 31) if f(s, 2)]))

#       Программа выведет:
#       2

# print([s for s in range(1, 31) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [6, 7, 8, 9, 10, 11]

# print(max([s for s in range(1, 31) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       13


#       № 23
#  (№ 7436)
# def f(x, y):
#     if x > y or x == 13: return 0
#     if x == y: return 1
#     return f(x + 2, y) + f(x * 3, y) + f(x ** 2, y)
# print(f(3, 49))

#       Программа выведет:
#       11

