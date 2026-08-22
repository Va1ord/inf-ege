#       Вариант 14.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = y and (x <= w) and ((not x) <= ((not w) == z))
#                 if f == 0:  #  Для решения задачи необходимо проверить оба условия: при f == 0 и f == 1
#                     print(x, y, z, w)

#       Программа выведет при f == 0:
#       x y z w
#       0 0 0 0
#       0 0 0 1
#       0 0 1 0
#       0 0 1 1
#       0 1 0 0
#       0 1 1 1
#       1 0 0 0
#       1 0 0 1
#       1 0 1 0
#       1 0 1 1
#       1 1 0 0
#       1 1 1 0

#       Программа выведет при f == 1:
#       x y z w
#       0 1 0 1
#       0 1 1 0
#       1 1 0 1
#       1 1 1 1


#       № 5
# w = []
# for n in range(1, 100):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s +='0'
#     else:
#         s += '1'
#     if s.count('1') % 3 == 0:
#         s = '11' + s[2:]
#     else:
#         s = '10' + s[2:]
#     r = int(s, 2)
#     if r <= 37:
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       25


#       № 6
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# up()
# fd(100 * m)
# rt(90)
# fd(100 * m)
# rt(45)
# down()
# for i in range(10):
#     fd(30 * m)
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
# for x in product('0123', repeat=5):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('3') == 1:
#             if '03' not in s and '30' not in s:
#                 k += 1
# print(k)

#       Программа выведет:
#       174


#       № 14
# x = 4 ** 2022 - 6 * 4 ** 522 + 5 * 64 ** 510 - 3 * 2 ** 330 - 100
# k = 0
# while x > 0:
#     if x % 8 == 7:
#         k += 1
#     x //= 8
# print(k)

#       Программа выведет:
#       1015


#       № 15
# def f(x):
#  return ((x % 20 == 0) <= (x % 11 != 0)) or (x + a >= 300)
#
# s = []
# for a in range(1, 500):
#     if all(f(x) == 1 for x in range(1, 500)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       80


#       № 16
# def f(n):
#     if n < 3:
#         return n
#     if n > 2 and n % 2 == 0:
#         return 3 * (n - 1) + f(n - 1) + 5
#     if n > 2 and n % 2 != 0:
#         return 3 * (n + 1) + f(n - 2) - 2
# print(f(35))

#       Программа выведет:
#       987


#       № 19 - 21
# def f(x, m):
#     if x >= 301: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 301) if f(s, 2)])

#       Программа выведет:
#       [150]

# print([s for s in range(1, 301) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [75, 149]

# print(min([s for s in range(1, 301) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       148


#       № 23
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 1, y)  + f(x // 2, y)
# print(f(60, 10) * f(10, 2))

#       Программа выведет:
#       1956

