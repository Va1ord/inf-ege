#       Вариант 2.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((z <= y) and ((not y) == x)) <= (not w)
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 1 0 1
#       0 1 1 1
#       1 0 0 1


#       № 5
# w = [ ]
# for n in range(1, 100):
#     s = bin(n)[2:]
#     if n % 3 == 0:
#         s += s[-3:]
#     else:
#         s = s + bin(((n % 3) - 1) * 3)[2:]
#     r = int(s, 2)
#     if r <= 416:
#         w.append(r)
# print(max(w))

#       Программа выведет:
#       411


#       № 5
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(4):
#     fd(19 * m)
#     lt(180)
#     bk(10 * m)
#     rt(90)
# up()
# bk(5 * m)
# lt(90)
# fd(4 * m)
# rt(90)
# down()
# for i in range(2):
#     fd(15 * m)
#     lt(90)
#     fd(8 * m)
#     lt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# for x in product(sorted('СТРЕЛА'), repeat=5):
#     s =''.join(x)
#     k += 1
#     if s[0] not in 'АСТ' and s.count('Е') == 2 and 'ЕЕ' not in s:
#         if k % 2 != 0:
#             print(k)

#       Программа выведет:
#       4295


#       № 14
# x = 4 * 2187 ** 2101 + 729 ** 2000 - 5 * 243 ** 2100 + 81 ** 2200 - 3 * 27 ** 2250 - 26244
# k = 0
# while x > 0:
#     if x % 27 > 9:
#         k += 1
#     x //= 27
# print(k)

#       Программа выведет:
#       3432


#       № 16
# f = {}
# for n in range(2026):
#     f[1] = 15
#     if n >= 2:
#         f[n] = 2 * f[n - 1] - n
# print((f[2025] - f[2023] - 2) // 2 ** 2022)

#       Программа выведет:
#       36


#       № 19 - 21
# def f(x, m):
#     if x <= 65: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x - 3, m - 1), f(x - 5, m - 1), f(x // 4, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(66, 300) if f(s, 2)]))

#       Программа выведет:
#       264

# print([s for s in range(66, 300) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [267, 268, 269, 270, 271]

# print(min([s for s in range(66, 300) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       272


#       № 23
# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     s = str(x)
#     if int(s[-1]) > int(s[1]):
#         return f(x + 1, y) + f(int(s[0] + s[2] + s[1]), y)
#     else:
#         return f(x + 1, y)
# print(f(110, 154))

#       Программа выведет:
#       34

