#       Вариант № 3.


#       № 2
#  	(№ 7533) (ЕГЭ-2024)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not(x <= z) or (y == w) or y
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       0 0 1 1
#       1 0 1 1


#       № 5
#  	(№ 7539) (ЕГЭ-2024)
# for n in range(1, 100):
#     s = bin(n)[2:]
#     for i in range(2):
#         if s.count('1') % 2 == 0:
#             s = s + '0'
#         else:
#             s = s + '1'
#     r = int(s, 2)
#     if r > 75:
#         print(r)
#         break

#       Программа выведет:
#       78


#       № 6
#  	(№ 7541) (ЕГЭ-2024)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(10):
#     fd(22 * m)
#     rt(90)
#     fd(16 * m)
#     rt(90)
# up()
# fd(1 * m)
# rt(90)
# fd(1 * m)
# lt(90)
# down()
# for i in range(10):
#     fd(72 * m)
#     rt(90)
#     fd(79 * m)
#     rt(90)
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7545) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('0123456789ABCDE', repeat=5):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('8') == 1:
#             s = s.replace('B', 'A').replace('C', 'A').replace('D', 'A').replace('E', 'A')
#             if s.count('A') >= 2:
#                 k += 1
# print(k)

#       Программа выведет:
#       83175


#       № 12
#  (№ 7521) (ЕГЭ-2024)
# s = 83 * '8'
# while '111' in s or '88888' in s:
#     if '111' in s:
#         s = s.replace('111', '88', 1)
#     else:
#         s = s.replace('88888', '8', 1)
# print(s)

#       Программа выведет:
#       888


#       № 13
#  (№ 7609)
# from itertools import *
# k = 0
# for x in product('01', repeat=10):
#     s = ''.join(x)
#     if (9 + s.count('1')) % 7 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       772


#       № 14
#  (№ 7671)
mx_x = 0  #  Максимальный x
mx_0 = 0  #  Максимальное количество нулей
for x in range(1000):
    n = 7 ** 400 + 7 ** 300 - x
    k = 0
    while n > 0:
        if n % 7 == 0:
            k += 1
        n //= 7
    if k >= mx_0:
        mx_0 = k
        mx_x = x
print(mx_0)

#       Программа выведет:
#


#       № 16
#  (№ 7562) (ЕГЭ-2024)
# f = {}
# for n in range(1, 2025):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = (n + 1) * f[n - 1]
# print((f[2024] + 3 * f[2023]) // f[2022])

#       Программа выведет:
#       4104672


#       № 17
#  (№ 7684)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17.txt')
# s = [int(x) for x in f]
# # print(s)  #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s)):
#     if s[i] % 10 == 1:
#         m.append(s[i])
# mx = max(m)
# for i in range(len(s) - 3):
#     k2 = 0
#     if s[i] < mx and s[i + 1] < mx and s[i + 2] < mx and s[i + 3] < mx:
#         if s[i] % 2 == 0:
#             k2 += 1
#         if s[i + 1] % 2 == 0:
#             k2 += 1
#         if s[i + 2] % 2 == 0:
#             k2 += 1
#         if s[i + 3] % 2 == 0:
#             k2 += 1
#         if k2 % 2 != 0:
#             k += 1
#             w.append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
# print(k, min(w))

#       Программа выведет:
#       117 559


#       № 19 - 21
#  (№ 7567) (ЕГЭ-2024)
# def f (x, m):
#     if x >= 39: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 3, m - 1), f(x * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(1, 39) if f(s, 2)]))

#       Программа выведет:
#       19

# print([s for s in range(1, 39) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [16, 18]

# print(min([s for s in range(1, 39) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       15


#       № 23
#  (№ 7571) (ЕГЭ-2024)
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 2, y) + f(x // 2, y)
# print(f(32, 8) * f(8, 1))

#       Программа выведет:
#       42

