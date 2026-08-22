#       Вариант 4.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not((((not y) == w) and (z <= x)) <= y)
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       1 0 0 1
#       1 0 1 1


#       № 5
# def l(k):
#     s = [int(x) for x in str(k)]
#     sm = sum(s)
#     m, n = max(s), min(s)
#     w = [sm - m, sm - n]
#     w.sort(reverse=True)
#     return int(str(w[0]) + str(w[1]))
#
# for k in range(1000, 10000):
#     if l(k) == 2013:
#         print(k)
#         break

#       Программа выведет:
#       1488


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(2):
#     fd(9 * m)
#     rt(90)
#     fd(5 * m)
#     rt(270)
# bk(18 * m)
# lt(90)
# fd(10 * m)
# rt(90)
# up()
# fd(5 * m)
# rt(90)
# fd(3 * m)
# lt(90)
# down()
# for i in range(4):
#     fd(8 * m)
#     rt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# for x in product(sorted('МОСКВА'), repeat=6):
#     s = ''.join(x)
#     k += 1
#     if s[0] not in 'АВК' and s.count('М') == 2:
#         if k % 2 != 0:
#             n = k
#             print(n)
#             break

#       Программа выведет:
#       23347


#       № 14
# x = 3 * 512 ** 1500 + 256 ** 1501 - 2 * 128 ** 1502 + 64 ** 1503 - 3 * 32 ** 1504 - 10240
# k = 0
# while x > 0:
#     if x % 32 <= 9:
#         k += 1
#     x //= 32
# print(k)

#       Программа выведет:
#       602


#       № 15
# def f(x, y):
#     return (201 != y + 2 * x) or (a > x) or (a > y)
#
# s = []
# for a in range(300):
#     if all(f(x, y) == 1 for x in range(300) for y in range(300)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       68


#       № 16
# def f(n):
#     if n < 10: return n
#     if n >= 10: return n ** 3 + f(n - 11)
# print(f(900) - f(856))

#       Программа выведет:
#       2760145884


#       № 19 - 21
# def f(x, m):
#     if x <= 76: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x - 3, m - 1), f(x - 5, m - 1), f(x // 4, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(77, 400) if f(s, 2)]))

#       Программа выведет:
#       308

# print([s for s in range(77, 400) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [311, 312, 313, 314, 315]

# print(min([s for s in range(77, 400) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       316


#       № 23
# def f(x, y):
#     if x < y or x == 7: return 0
#     if x == y: return 1
#     return f(x - 1, y) + f(x - 4, y) + f(x // 2, y)
# print(f(25, 10) * f(10, 3))

#       Программа выведет:
#       546

