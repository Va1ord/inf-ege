#       Вариант № 11.


#       № 2
#  (№ 6692)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x <= y) and ((not y) == z) and w
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 1
#       0 1 0 1
#       1 1 0 1


#       № 5
#  (№ 7385)
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
#         s = s + f((n % 4) * 5)
#     r = int(s, 4)
#     if r < 555:
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       34


#       № 6
#  (№ 7358)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(5):
#     rt(45)
#     fd(10 * m)
#     rt(45)
# for i in range(6):
#     fd(20 * m)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7387)
# from itertools import *
# k = 0
# n = 0
# for x in product(sorted('КОМПАНИЯ'), repeat=6):
#     s = ''.join(x)
#     k += 1
#     if s[0] != 'М' and s.count('И') == 3:
#         if k % 2 != 0:
#             n += 1
# print(n)

#       Программа выведет:
#       1848


#       № 12
#  (№ 6596)
# for n in range(3, 1000):
#     s = '2' + n * '5'
#     while '25' in s or '35' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '53', 1)
#         if '35' in s:
#             s = s.replace('35', '2', 1)
#         if '555' in s:
#             s = s.replace('555', '23', 1)
#     if sum([int(i) for i in s]) % 7 == 0:
#         print(n)
#         break

#       Программа выведет:
#       21


#       № 14
#  (№ 7523) (ЕГЭ-2024)
# mx_x = 0  #  Максимальный x
# for x in range(1, 2031):
#     n = 7 ** 91 + 7 ** 160 - x
#     k = 0
#     while n > 0:
#         if n % 7 == 0:
#             k += 1
#         n //= 7
#     if k == 70:
#         mx_x = x
# print(mx_x)

#       Программа выведет:
#       2029


#       № 15
#  (№ 6749) (ЕГЭ-2023)
# def f(x, y):
#     return (x + 2 * y > a) or (y < x) or (x < 30)
# s = []
# for a in range(0, 300):
#     if all(f(x, y) == 1 for x in range(0, 300) for y in range(0, 300)):
#         s.append(a)
# print(max(s))

#       Программа выведет:
#       89


#       № 17
#  (№ 7487) (ЕГЭ-2024)
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
#     if ((s[i] % 77) * (s[i + 1] % 77)) == mn ** 2:
#         k += 1
#         w.append(s[i] * s[i + 1])
# print(k, min(w))

#       Программа выведет:
#       48 5952


#       № 19 - 21
#  (№ 6769) (ЕГЭ-2023)
# def f(x, m):
#     if x >= 111: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 3, m - 1), f(x * 4, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 111) if f(s, 2)])

#       Программа выведет:
#       [27]

# print([s for s in range(1, 111) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [24, 26]

# print(min([s for s in range(1, 111) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       23


#       № 23
#  (№ 7208)
# def f(x, y):
#     if x > y or x == 17 or x == 32 or x == 50: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x + 5, y) + f(x ** 2, y)
# print(f(5, 25) * f(25, 45) * f(45, 60))

#       Программа выведет:
#       71280

