#       Вариант № 17.


#       № 2
#  (№ 6615)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= y) or(z == x)) and (w <= z)
#                 if f == 1:  #  Для решения задачи необходимо проверить оба условия: при f == 0 и f == 1
#                     print(x, y, z, w)

#       Программа выведет при f == 0:
#       x y z w
#       0 0 0 1
#       0 1 0 1
#       1 0 0 0
#       1 0 0 1
#       1 1 0 1

#       Программа выведет при f == 1:
#       x y z w
#       0 0 0 0
#       0 0 1 0
#       0 0 1 1
#       0 1 0 0
#       0 1 1 0
#       0 1 1 1
#       1 0 1 0
#       1 0 1 1
#       1 1 0 0
#       1 1 1 0
#       1 1 1 1


#       № 5
#  (№ 6998)
# for n in range(1, 1000):
#     s = bin(n)[2:]
#     if s.count('1') % 2 == 0:
#         s = '1' + s + '00'
#     else:
#         s = '11' + s
#     r = int(s, 2)
#     if r >= 412:
#         print(n)
#         break

#       Программа выведет:
#       39


#       № 6
#  (№ 6713) (ЕГЭ-2023)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(2):
#     fd(13 * m)
#     rt(90)
#     fd(20 * m)
#     rt(90)
# up()
# fd(8 * m)
# rt(90)
# bk(3 * m)
# lt(90)
# down()
# for i in range(2):
#     fd(16 * m)
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
#  (№ 7170)
# from itertools import *
# k = 0
# for x in product(sorted('БЭПН'), repeat=4):
#     s = ''.join(x)
#     k += 1
#     if s[0] != 'П' and s[-1] != 'П' and 'ЭЭ' not in s:
#         if k % 2 == 0:
#             n = k
# print(n)

#       Программа выведет:
#       238


#       № 12
#  (№ 6113)
# for n in range(1, 500):
#     s = '9' + n * '1' + n * '2'
#     while '91' in s or '92' in s:
#         if '91' in s:
#             s = s.replace('91', '39', 1)
#         if '92' in s:
#             s = s.replace('92', '59', 1)
#     sm = sum([int(i) for i in s])
#     if sm > 100:
#         print(sm, n)

#       Программа выведет:
#       105 12
#       113 13 ... 113 - простое число


#       № 14



#       № 16
#  (№ 6756) (ЕГЭ-2023)
# f = {}
# for n in range(3030):
#     if n < 3:
#         f[n] = 3
#     if n >= 3:
#         f[n] = 2 * n + 5 + f[n - 2]
# print(f[3027] - f[3023])

#       Программа выведет:
#       12114


#       № 19 - 21
#  (№ 6496)
def f(x, y, m):
    if x or y >= 78: return m % 2 == 0
    if m == 0: return 0
    h = []
    if x == y:
        h.append([f(x + 1, y, m - 1), f(x + 2, y, m - 1), f(x + 3, y, m - 1),
                  f(x, y + 1, m - 1), f(x, y + 2, m - 1), f(x, y + 3, m - 1)])
    elif x < y:
        h.append([f(x + 1, y, m - 1), f(x + 2, y, m - 1), f(x + 3, y, m - 1),
                  f(x, y + 1, m - 1), f(x, y + 2, m - 1), f(x, y + 3, m - 1),
                  f(x * 2, y, m - 1)])
    elif x < y:
        h.append([f(x + 1, y, m - 1), f(x + 2, y, m - 1), f(x + 3, y, m - 1),
                  f(x, y + 1, m - 1), f(x, y + 2, m - 1), f(x, y + 3, m - 1),
                  f(x, y * 2, m - 1)])
    if m % 2 != 0:
        return any(h)
    return all(h)

print([s for s in range(1, 78) if not f(25, s, 1) and f(25, s, 3)])

#       Программа выведет:
#

print([s for s in range(1, 78) if not f(69, s, 2) and f(69, s, 4)])

#       Программа выведет:
#       29


#       № 23
#  (№ 7117)
# def f(x, y):
#     if x < y or x == 19: return 0
#     if x == y: return 1
#     return f(x - 2, y) + f(x - 1, y) + f(x // 2, y)
# print(f(36, 16) * f(16, 15) * f(15, 12))

#       Программа выведет:
#       9621

