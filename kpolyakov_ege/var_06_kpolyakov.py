#       Вариант № 6.


#       № 2
#  (№ 7454) (ЕГЭ-2024)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not(x <= w) or (y <= z) or (not y)
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 1 0 0
#       0 1 0 1
#       1 1 0 1


#       № 5
#  	(№ 7456) (ЕГЭ-2024)
# for n in range(1, 1000):
#     s = bin(n)[2:]
#     if s.count('1') % 2 == 0:
#         s = '10' + s[2:] + '0'
#     else:
#         s = '11' + s[2:] +'1'
#     r = int(s, 2)
#     if r > 50:
#         print(n)
#         break

#       Программа выведет:
#       19


#       № 6
#  (№ 7459) (ЕГЭ-2024)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(4):
#     fd(28 * m)
#     rt(90)
#     fd(26 * m)
#     rt(90)
# up()
# fd(8 * m)
# rt(90)
# fd(7 * m)
# lt(90)
# down()
# for i in range(4):
#     fd(67 * m)
#     rt(90)
#     fd(98 * m)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7463) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('01234567', repeat=5):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s[0] not in '1357' and s[-1] not in '26' and s.count('7') <= 2:
#             k += 1
# print(k)

#       Программа выведет:
#       9135


#       № 12
#  	(№ 6824) (ЕГЭ-2023)
# for n in range(3, 10001):
#     s = '1' + n * '8'
#     while '18' in s or '388' in s or '888' in s:
#         if '18' in s:
#             s = s.replace('18', '8', 1)
#         if '388' in s:
#             s = s.replace('388', '81', 1)
#         if '888' in s:
#             s = s.replace('888', '3', 1)
#     if s.count('1') == 3:
#         print(n)
#         break

#       Программа выведет:
#       33


#       № 13
#  	(№ 7556) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('01', repeat=17):
#     s = ''.join(x)
#     if (9 + s.count('1')) % 5 == 0:
#         k += 1
# print(k)

#       Программа выведет:
#       24786


#       № 14
#  (№ 7073) (PRO100-ЕГЭ)
# for x in range(1, 1000):
#     n = 4 * 625 ** 1920 + 4 * 125 ** x - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
#     k = 0
#     while n > 0:
#         if n % 5 == 0:
#             k += 1
#         n //= 5
#     if k == 1891:
#         print(x)
#         break

#       Программа выведет:
#       20


#       № 15
#  (№ 7266)
def f(x, y):
    return (3 * x + 2 * y > 95) or (4 * x < 3 * y) or (x + 4 * y < a)

s = []
for a in range(300):
    if all(f(x, y) == 0 for x in range(300) for y in range(300)):
        s.append(a)
print(max(s))

#       Программа выведет:
#


#       № 16
#  	(№ 7488) (ЕГЭ-2024)
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = 3 * n * f[n - 1]
# print((f[2024] // 6 + f[2023]) // f[2022])

#       Программа выведет:
#       6147897


#       № 17
#  (№ 7681)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17.txt')
# s = [int(x) for x in f]
# # print(s)   #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s)):
#     if s[i] % 10 == 7:
#         m.append(s[i])
# mx = max(m)
# for i in range(len(s) - 1):
#     s1 = str(s[i])
#     s2 = str(s[i + 1])
#     if (s1[0] == s2[0]) and ((s[i] % 10 == 7) or (s[i + 1] % 10 == 7)) and (99 < s[i] < 1000 or 99 < s[i + 1] < 1000):
#         if (s[i] + s[i + 1]) < mx:
#             k += 1
#             w.append(s[i] + s[i + 1])
# print(k, max(w))

#       Программа выведет:
#       3 1027


#       № 19 - 21
#  (№ 7384)
def f(x, m):
    if x >= 61: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 1, m - 1), f(x * 2, m - 1)]
    if m % 2 != 0:
        return any(h)
    else:
        return all(h)

print([s for s in range(1, 61) if f(s, 1)])

#       Программа выведет:
#

# print([s for s in range(1, 61) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [15, 29]

print([s for s in range(1, 61) if not f(s, 2) and f(s, 4)])

#       Программа выведет:
#


#       № 23
#  (№ 7492) (ЕГЭ-2024)
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 1, y) + f(x - 2, y) + f(x // 3, y)
# print(f(16, 11) * f(11, 6))

#       Программа выведет:
#       64

