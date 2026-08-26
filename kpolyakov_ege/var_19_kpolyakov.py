#       Вариант № 19.


#       № 2
#  (№ 6579)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((w <= z) == y) <= x
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       0 1 0 0
#       0 1 1 0
#       0 1 1 1


#       № 6
#  (№ 6711)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 10
# lt(90)
# for i in range(2):
#     fd(5 * m)
#     rt(90)
#     fd(11 * m)
#     rt(90)
# up()
# bk(4 * m)
# rt(90)
# fd(6 * m)
# lt(90)
# down()
# for i in range(2):
#     fd(42 * m)
#     rt(90)
#     fd(63 * m)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 12
#  (№ 5914)
# for n in range(1, 100):
#     s = 15 * '3' + 18 * '2' + n * '1'
#     while '31' in s or '33' in s or '21' in s:
#         if '31' in s:
#             s = s.replace('31', '123', 1)
#         if '33' in s:
#             s = s.replace('33', '211', 1)
#         if '21' in s:
#             s = s.replace('21', '1', 1)
#     if sum([int(i) for i in s]) > 24:
#         print(n)
#         break

#       Программа выведет:
#       6


#       № 14
#  (№ 7275)
# for x in range(1, 20):
#     for y in range(19):
#         for z in range(1, 20):
#             for w in range(19):
#                 for p in range(11, 15):
#                     s1 = [8, x, y, x, z]
#                     s2 = [7, 1, 5, y, x]
#                     s3 = [2, 6, x, z, w]
#                     d1 = 0
#                     d2 = 0
#                     d3 = 0
#                     for i in range(5):
#                         d1 += s1[i] * p ** i
#                         d2 += s2[i] * p ** i
#                         d3 += s3[i] * p ** i
#                     if (d1 + d2) == d3:
#                         print(x, y, z, w, p)

#       Программа выведет:
#       4 12 4 9 13

# print(4 * 13 ** 3 + 12 * 13 ** 2 + 4 * 13 + 9)

#       Программа выведет:
#       10877


#       № 16
#  (№ 6754) (ЕГЭ-2023)
# f = {}
# for n in range(1, 2025):
#     if n < 11:
#         f[n] = n
#     if n >= 11:
#         f[n] = n + f[n - 1]
# print(f[2024] - f[2021])

#       Программа выведет:
#       6069


#       № 17
#  (№ 6759) (ЕГЭ-2023)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17.txt')
# s = [int(x) for x in f]
# # print(s)  #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s)):
#     if 999 < abs(s[i]) < 10000:
#         if abs(s[i]) % 100 == 39:
#             m.append(s[i])
# mx = max(m)
# for i in range(len(s) - 1):
#     if (999 < abs(s[i]) < 10000) + (999 < abs(s[i + 1]) < 10000) == 1 and (s[i] + s[i + 1]) ** 2 <= mx ** 2:
#         k += 1
#         w.append(s[i] + s[i + 1])
# print(k, max(w))

#       Программа выведет:
#       1591 9233


#       № 19 - 21
#  (№ 6346)
def f(x, y, m):
    if x + y >= 60: return m % 2 == 0
    if m == 0: return 0
    h = []
    if x > y:
        h.append(f(x + 1, y, m - 1))
        h.append(f(x + 2, y, m - 1))
        h.append(f(x + 3, y, m - 1))
        h.append(f(x * 3, y, m - 1))
    if x < y:
        h.append(f(x, y + 1, m - 1))
        h.append(f(x, y + 2, m - 1))
        h.append(f(x, y + 3, m - 1))
        h.append(f(x, y * 3, m - 1))
    if x == y:
        h.append(f(x + 1, y, m - 1))
        h.append(f(x + 2, y, m - 1))
        h.append(f(x + 3, y, m - 1))
        h.append(f(x, y + 1, m - 1))
        h.append(f(x, y + 2, m - 1))
        h.append(f(x, y + 3, m - 1))
    if m % 2 != 0:
        return any(h)
    else:
        return any(h)


#       № 23
#  (№ 7101)
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 3, y) + f(x - 2, y) + f(x - 1, y)
# print(f(36, 28) * f(28, 26) * f(26, 13))

#       Программа выведет:
#       276210

