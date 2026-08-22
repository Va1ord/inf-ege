#       Вариант 13.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = x and (y <= z) and ((not y) <= ((not z) == w))
#                 if f == 0:  #  Для решения задачи необходимо проверить оба условия: при f == 0 и f == 1
#                     print(x, y, z, w)

#       Программа выведет при f == 0:
#       x y z w
#       0 0 0 0
#       0 0 0 1
#       0 0 1 0
#       0 0 1 1
#       0 1 0 0
#       0 1 0 1
#       0 1 1 0
#       0 1 1 1
#       1 0 0 0
#       1 0 1 1
#       1 1 0 0
#       1 1 0 1

#       Программа выведет при f == 1:
#       x y z w
#       1 0 0 1
#       1 0 1 0
#       1 1 1 0
#       1 1 1 1


#       № 5
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
#     if r >= 26:
#         print(n)
#         break

#       Программа выведет:
#       9


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
# rt(90)
# rt(30)
# down()
# for i in range(10):
#     fd(25 * m)
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
# for x in product('01234567', repeat=5):
#     s = ''.join(x)
#     if s[0] != '0':
#         if s.count('4') == 2:
#             s = s.replace('3', '1').replace('5', '1').replace('7', '1')
#             if '14' not in s and '41' not in s:
#                 k += 1
# print(k)

#       Программа выведет:
#       612


#       № 14
# x = 4 * 25 ** 2022 - 2 * 5 ** 2000 + 125 ** 1011 - 3 * 5 ** 100 - 660
# k = 0
# while x > 0:
#     if x % 5 == 4:
#         k += 1
#     x //= 5
# print(k)

#       Программа выведет:
#       3028


#       № 15
# def f(x):
#  return ((x % 13 == 0) <= (x % 21 != 0)) or (x + a >= 500)
#
# s = []
# for a in range(1, 700):
#     if all(f(x) == 1 for x in range(1, 700)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       227


#       № 16
# def f(n):
#     if n < 3:
#         return n
#     if n > 2 and n % 2 == 0:
#         return 2 * (n - 1) + f(n - 1) + 2
#     if n > 2 and n % 2 != 0:
#         return 2 * (n + 1) + f(n - 2) - 5
# print(f(32))

#       Программа выведет:
#       530


#       № 19 - 21
# def f(x, m):
#     if x >= 229: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 229) if f(s, 2)])

#       Программа выведет:
#       [114]

# print([s for s in range(1, 229) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [57, 113]

# print(min([s for s in range(1, 229) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#           112


#       № 23
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 1, y)  + f(x // 2, y)
# print(f(50, 20) * f(20, 1))

#       Программа выведет:
#       2340

