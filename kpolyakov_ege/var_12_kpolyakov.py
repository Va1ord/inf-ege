#       Вариант № 12.


#       № 2
#  (№ 6691)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (z == (not y)) and ((not x) or y) and w
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 1
#       0 1 0 1
#       1 1 0 1


#       № 5
#  (№ 7370)
# w = []
# for n in range(0, 256):
#     s = bin(n)[2:].zfill(8)
#     s = s.replace('1', '*')
#     s = s.replace('0', '1')
#     s = s.replace('*', '0')
#     if int(s, 2) % 5 == 0:
#         s = '100' + s[3:]
#     else:
#         s = '101' + s[3:]
#     r = int(s, 2)
#     if r == 180:
#         w.append(n)
# print(len(w))

#       Программа выведет:
#       6


#       № 6
#  (№ 6911)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 10
# lt(90)
# for i in range(2):
#     fd(16 * m)
#     rt(90)
#     fd(9 * m)
#     rt(90)
# up()
# fd(5 * m)
# rt(90)
# fd(11 * m)
# rt(90)
# down()
# for i in range(2):
#     fd(20 * m)
#     rt(90)
#     fd(8 * m)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7357)
# from itertools import *
# k = 0
# for x in  product('567', repeat=12):
#     s = ''.join(x)
#     if '55' not in s:
#         k += 1
# print(k)

#       Программа выведет:
#       186304


#       № 12
#  (№ 6569)
# for n in range(1, 1000):
#     s = '>' + 21 * '0' + n * '1' + 11 * '2'
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     if (s.count('1') + s.count('2') * 2) % n == 0:
#         print(n)

#       Программа выведет:
#       1  #  Число 1 не является простым числом, так как у него только один делитель — 1
#       43


#       № 14
#  (№ 7069)
# for x in '0123456789ABC':
#     s1 = '615' + x + '483'
#     s2 = '85996' + x + '262'
#     s3 = '62421' + x
#     s4 = '45' + x + '61584' + x
#     f = int(s1, 13) + int(s2, 13) + int(s3, 13) + int(s4, 13)
#     if f % 12 == 0:
#         print(x, f // 12)

#       Программа выведет:
#       2 875575783


#       № 15
#  (№ 6748) (ЕГЭ-2023)
# def f(x, y):
#     return (x * y < a) or (x < y) or (9 < x)
# s = []
# for a in range(0, 300):
#     if all(f(x, y) == 1 for x in range(0, 300) for y in range(0, 300)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       82


#       № 17
#  (№ 7486) (ЕГЭ-2024)
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
#     if s[i] % 65 == mn and s[i + 1] % 65 == mn:
#         k += 1
#         w.append(s[i] + s[i + 1])
# print(k, max(w))

#       Программа выведет:
#       19 125644


#       № 19 - 21
#  (№ 6768) (ЕГЭ-2023)
# def f(x, m):
#     if x >= 59: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 4, m - 1), f(x * 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 59) if f(s, 2)])

#       Программа выведет:
#       [19]

# print([s for s in range(1, 59) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [15, 18]

# print(min([s for s in range(1, 59) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       14


#       № 23
#  (№ 7207)
# def f(x, y):
#     if x > y or x == 15 or x == 30: return 0
#     if x == y: return 1
#     return f(x + 2, y) + f(x + 3, y) + f(x ** 2, y)
# print(f(3, 10) * f(10, 20) * f(20, 38))

#       Программа выведет:
#       333

