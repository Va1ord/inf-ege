#       Вариант 17.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not((x <= y) <= w) and z
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       0 1 1 0
#       1 1 1 0


#       № 5
# w = []
# for n in range(100, 1000):
#     s = str(n)
#     x1 = int(s[0]) ** 2 + int(s[1]) ** 2
#     x2 = int(s[1]) ** 2 + int(s[2]) ** 2
#     sm = str(max(x1, x2)) + str(min(x1, x2))
#     if sm == '9752':
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       946


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 10
# lt(90)
# for i in range(11):
#     fd(111 * m)
#     rt(120)
# up()
# for x in range(-70, 100):
#     for y in range(-100, 100):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# for x in product(sorted('АТОМ'), repeat=4):
#     s = ''.join(x)
#     k += 1
#     if s[0] == 'О':
#         print(k)
#         break

#       Программа выведет:
#       129


#       № 14
# x = 5 ** 2022 - 2 * 5 ** 1010 + 25 ** 850 + 2500
# k = 0
# while x > 0:
#     if x % 5 == 4:
#         k += 1
#     x //= 5
# print(k)

#       Программа выведет:
#       690


#       № 16
# def f(n):
#     if n <= 1:
#         return 1
#     if n > 1 and n % 2 != 0:
#         return 5 * n + f(n - 1) + f(2)
#     if n > 1 and n % 2 == 0:
#         return 3 * f(n - 1)
# print(f(23))

#       Программа выведет:
#       2214271


#       № 19 - 21
# def f(x, y, m):
#     if x + y >= 145: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, y, m - 1), f(x, y + 1, m - 1), f(x * 2, y, m - 1), f(x, y * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return any(h)  #  В 21 и 22 задании поменяйте на all(h)

# print(min([s for s in range(1, 138) if f(7, s, 2)]))

#       Программа выведет:
#       35

# print([s for s in range(1, 138) if not f(7, s, 1) and f(7, s, 3)])

#       Программа выведет:
#       [65, 68]

# print(min([s for s in range(1, 138) if not f(7, s, 2) and f(7, s, 4)]))

#       Программа выведет:
#       64


#       № 23
# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     return f(x + 2, y) + f(x + 7, y)
# print(f(5, 49))

#       Программа выведет:
#       639

