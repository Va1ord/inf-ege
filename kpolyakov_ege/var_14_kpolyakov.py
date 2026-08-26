#       Вариант № 14.


#       № 2
#  (№ 6689) (ЕГЭ-2023)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       0 1 1 0
#       1 1 0 0


#       № 5
#  (№ 7054) (PRO100-ЕГЭ)
# def f(n):
#     s = ''
#     while n > 0:
#         s += str(n % 6)
#         n //= 6
#     return s[::-1]
#
# for n in range(1, 1000):
#     s = f(n)
#     if n % 3 == 0:
#         s += s[:2]
#     else:
#         s = s + f((n % 3) * 10)
#     r = int(s, 6)
#     if r > 680:
#         print(r)
#         break

#       Программа выведет:
#       694


#       № 6
#  (№ 6894)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# x = 3
# lt(90)
# fd(x * m)
# for i in range(3):
#     fd((3 * x) * m)
#     rt(90)
# lt(90)
# for i in range(3):
#     fd(x * m)
#     rt(90)
# lt(180)
# fd(x * m)
# lt(90)
# for i in range(2):
#     fd(x * m)
#     rt(90)
# up()
# fd((2 * x) * m)
# rt(90)
# fd(x * m)
# lt(90)
# down()
# for i in range(4):
#     fd(x * m)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 12
#  (№ 6236) (PRO100 ЕГЭ)
# for n in range(1, 1000):
#     s = '>' + 12 * '0' + n * '1' + 8 * '2'
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     if (s.count('1') + s.count('2') * 2) == 68:
#         print(n)

#       Программа выведет:
#       10


#       № 14
#  	(№ 7477) (ЕГЭ-2024)
# for x in range(4100, 10000):
#     n = 3 ** 100 - x
#     k = 0
#     while n > 0:
#         if n % 3 == 0:
#             k += 1
#         n //= 3
#     if k == 1:
#         print(x)
#         break

#       Программа выведет:
#       4375


#       № 15
#  (№ 6566)
# def f(x, y):
#     return (x >= 27) or ((2 * x) < (3 * y)) or (a > (x + 2) * (y - 3))
# s = []
# for a in range(0, 500):
#     if all(f(x, y) == 1 for x in range(0, 500) for y in range(0, 500)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       393


#       № 17
#  (№ 7484) (ЕГЭ-2024)
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
#     if ((s[i] % 18) + (s[i + 1] % 18)) == mn:
#         k += 1
#         w.append(s[i] + s[i + 1])
# print(k, max(w))

#       Программа выведет:
#       637 183452


#       № 19 - 21
#  (№ 6647)
# def f(x, y, m):
#     if x * y >= 123: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 2, y, m - 1), f(x, y + 2, m - 1), f(x * 2, y, m - 1), f(x, y * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return any(h)  #  В 21 и 22 задании поменяйте на all(h)

# print(max([s for s in range(1, 41) if f(3, s, 2)]))

#       Программа выведет:
#       38

# print([s for s in range(1, 41) if not f(3, s, 1) and f(3, s, 3)])

#       Программа выведет:
#       [9, 10, 11, 12, 17, 18]

# print(max([s for s in range(1, 41) if not f(3, s, 2) and f(3, s, 4)]))

#       Программа выведет:
#       16


#       № 23
#  (№ 7205)
# def f(x, y):
#     if x > y or x == 20 or x == 25: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x * 2, y) + f(x ** 2, y)
# print(f(2, 15) * f(15, 35) * f(35, 50))

#       Программа выведет:
#       57

