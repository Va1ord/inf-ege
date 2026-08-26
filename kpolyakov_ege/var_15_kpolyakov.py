#       Вариант № 15.


#       № 2
#  (№ 6688) (ЕГЭ-2023)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x or (not y)) and (not (x == z)) and (not w)
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       1 0 0 0
#       1 1 0 0


#       № 5
#  (№ 7000)
#  Видеоразбор https://rutube.ru/video/26943bb8797c89a8a19dfd7a28c06abc/
# r = 21
# n = f'{r:b}'
# n = n[1:-2] if n[-2:] == '00' else n[2:-1]
# s = int(n, 2)
# print(s)

#       Программа выведет:
#       2

# w = [100_000_001, 100_000_010, 100_000_100, 100_001_000, 100_010_000, 100_100_000, 101_000_000, 110_000_000, 200_000_000]
# print(len(w))

#       Программа выведет:
#       9


#       № 6
#  (№ 6813)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(3):
#     lt(90)
#     for j in range(4):
#         fd(5 * m)
#         rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 12
#  (№ 6235) (PRO100 ЕГЭ)
# for n in range(1, 1000):
#     s = '>' + 39 * '0' + n * '1' + 39 * '2'
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     sm = s.count('1') + s.count('2') * 2
#     print(sm, n)

#       Программа выведет:
#       121 1
#       125 2
#       129 3
#       133 4
#       137 5 ... 137 - простое число


#       № 14
#  (№ 7476) (ЕГЭ-2024)
# mx_x = 0  #  Максимальный x
# for x in range(1, 3001):
#     n = 7 ** 100 - x
#     k = 0
#     while n > 0:
#         if n % 7 == 0:
#             k += 1
#         n //= 7
#     if k == 2:
#         mx_x = x
# print(mx_x)

#       Программа выведет:
#       2989


#       № 15
#  (№ 6518)
# def f(x ,y):
#     return (11 <= y) or (7 * y < x) or (a > x * y)
# s = []
# for a in range(0, 800):
#     if all(f(x ,y) == 1 for x in range(0, 800) for y in range(0, 800)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       701


#       № 16
#  (№ 7077) (PRO100-ЕГЭ)
# def f(n):
#     return g(n - 1)
#
# def g(n):
#     if n < 10:
#         return n
#     if n >= 10:
#         return g(n - 2) + 1
#
# k = 0
# for i in range(1, 101):
#     for j in range(1, 101):
#         if f(i) == j ** 2:
#             k += 1
# print(k)

#       Программа выведет:
#       12


#       № 17
#  (№ 7429)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17.txt')
# s = [int(x) for x in f]
# # print(s)   #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s)):
#     if 9 < s[i] < 100 and s[i] % (s[i] // 10 + s[i] % 10) == 0:
#         m.append(s[i])
# mn = min(m)
# for i in range(len(s) - 1):
#     if s[i] % mn == 0 or s[i + 1] % mn == 0:
#         k += 1
#         w.append(s[i] + s[i + 1])
# print(k, max(w))

#       Программа выведет:
#       537 19247


#       № 19 - 21
#  (№ 6603)
# def f(x, m):
#     if x == 0: return m % 2 == 0
#     if m == 0: return 0
#     h = []
#     if x >= 5:
#         h.append(f(x - 5, m - 1))
#     if x % 3 != 0:
#         h.append(f(x // 3, m - 1))
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(max([s for s in range(1, 100) if f(s, 2)]))

#       Программа выведет:
#       7

# print([s for s in range(1, 100) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [8, 9, 10, 11, 12, 13, 14, 19, 20, 22, 23]

# print(max([s for s in range(1, 100) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       28


#       № 23
#  (№ 7204)
# def f(x ,y):
#     if x > y or x == 20: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x + 3, y) + f(x ** 2, y)
# print(f(2, 15) * f(15, 35))

#       Программа выведет:
#       70470

