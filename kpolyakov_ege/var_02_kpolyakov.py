#       Вариант № 2.


#       № 2
#  (№ 7534) (ЕГЭ-2024)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (not(x) and y and z and (not w)) or (not(x) and y and (not z) and not(w)) or (x and y and z and (not w))
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 1 0 0
#       0 1 1 0
#       1 1 1 0


#       № 5
#  (№ 7540) (ЕГЭ-2024)
# for n in range(1, 100):
#     s = bin(n)[2:]
#     for i in range(2):
#         if s.count('1') % 2 == 0:
#             s = s + '0'
#         else:
#             s = s + '1'
#     r = int(s, 2)
#     if r > 123:
#         print(r)
#         break

#       Программа выведет:
#       126


#       № 6
#  (№ 7542) (ЕГЭ-2024)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(2):
#     fd(6 * m)
#     rt(90)
#     fd(12 * m)
#     rt(90)
# up()
# fd(1 * m)
# rt(90)
# fd(3 * m)
# lt(90)
# down()
# for i in range(2):
#     fd(77 * m)
#     rt(90)
#     fd(45 * m)
#     rt(90)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7546) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('0123456789ABCD', repeat=5):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('9') == 1:
#             s = s.replace('C', 'B').replace('D', 'B')
#             if s.count('B') <= 3:
#                 k += 1
# print(k)

#       Программа выведет:
#       133612


#       № 12
#  (№ 7553) (ЕГЭ-2024)
# s = 136 * '9'
# while '22222' in s or '9999' in s:
#     if '22222' in s:
#         s = s.replace('22222', '99', 1)
#     else:
#         s = s.replace('9999', '2', 1)
# print(s)

#       Программа выведет:
#       2299


#       № 13
#  (№ 7610)
# from itertools import *
# k = 0
# for x in product('01', repeat=12):
#     s = ''.join(x)
#     if (9 + s.count('1')) % 6 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       3656


#       № 14
#  (№ 7672)
# mx_x = 0  #  Максимальный x
# mx_4 = 0  #  Максимальное количество четвёрок
# for x in range(60000, 70000):
#     n = 5 ** 2025 + 5 ** 400 - x
#     k = 0
#     while n > 0:
#         if n % 5 == 4:
#             k += 1
#         n //= 5
#     if k >= mx_4:
#         mx_4 = k
#         mx_x = x
# print(mx_x)

#       Программа выведет:
#       62501


#       № 15
#  (№ 7559) (ЕГЭ-2024)
# def f(x):
#     return (x % 33 == 0) <= ((x % a != 0) <= (x % 242 != 0))
# s = []
# for a in range(1, 1000):
#     if all(f(x) == 1 for x in range(1, 1000)):
#         s.append(a)
# print(max(s))

#       Программа выведет:
#       726


#       № 16
#  (№ 7602)
# f = {}
# for n in range(2030):
#     if n < 3:
#         f[n] = 1
#     if n > 2:
#         f[n] = f[(n + 1) // 2] + 1
# print(f[2025])

#       Программа выведет:
#       11


#       № 17
#  (№ 7685)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# from math import *
# f = open('17.txt')
# s = [int(x) for x in f]
# # print(s)  #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s) - 1):
#     w.append(gcd(s[i], s[i + 1]))
# m = sorted(set(w))
# for i in range(len(m)):
#     if m[i] in w:
#         k = w.count(m[i])
# sm = []
# for i in range(len(s) - 1):
#     if gcd(s[i], s[i + 1]) == 17:
#         sm.append(s[i] + s[i + 1])
# print(max(sm))

#       Программа выведет:
#       1649


#       № 19 - 21
#  	(№ 7568) (ЕГЭ-2024)
# def f(x, y, m):
#     if x + y >= 227: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, y, m - 1) , f(x, y + 1, m - 1), f(x * 2, y, m - 1), f(x, y * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return any(h)  #  В 21 и 22 задании поменяйте на all(h)

# print(min([s for s in range(1, 210) if f(17, s, 2)]))

#       Программа выведет:
#       53

# print([s for s in range(1, 210) if not f(17, s, 1) and f(17, s, 3)])

#       Программа выведет:
#       [96, 104]

# print(min([s for s in range(1, 210) if not f(17, s, 2) and f(17, s, 4)]))

#       Программа выведет:
#       95

#       № 23
#  (№ 7572) (ЕГЭ-2024)
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 2, y) + f(x // 2, y)
# print(f(32, 14) * f(14, 1))

#       Программа выведет:
#       54

