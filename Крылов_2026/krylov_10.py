#       Вариант 10.


#       № 2
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not(y <= x) or (y == w) or z
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       1 0 0 1
#       1 1 0 0


#       № 5
# def f(n):
#     s = ''
#     while n > 0:
#         s += str(n % 4)
#         n //= 4
#     return s[::-1]
#
# w = []
# for n in range(1, 100):
#     s = f(n)
#     if n % 4 == 0:
#         s += s[-2:]
#     else:
#         s = s + f((n % 4) * 2)
#     r = int(s, 4)
#     if r < 369:
#         w.append(n)
# print(max(w))


#       Программа выведет:
#       89


#       № 5
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(2):
#     fd(15 * m)
#     lt(90)
#     fd(20 * m)
#     lt(90)
# up()
# rt(90)
# bk(7 * m)
# lt(90)
# bk(9 * m)
# down()
# for i in range(2):
#     fd(17 * m)
#     rt(90)
#     fd(15 * m)
#     rt(90)
# up()
# for x in range(-20, 10):
#     for y in range(-10, 20):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
# from itertools import *
# k = 0
# n = 0
# for x in product(sorted('РЕПЛИКА'), repeat=6):
#     s = ''.join(x)
#     k += 1
#     if s[0] != 'К' and s.count('И') >= 2:
#         if k % 2 == 0:
#             n += 1
# print(n)

#       Программа выведет:
#       10892


#       № 14
# for x in '0123456789ABCDEFGHIJKLM':
#     s1 = '2' + x + x + '341011'
#     s2 = '220' + x + '4'
#     s3 = '110' + x + '6'
#     sm = int(s1, 23) + int(s2, 23) + int(s3, 23)
#     if sm % 22 == 0:
#         print(x, sm // 22)
#         break

#       Программа выведет:
#       4 7766124214


#       № 15
# def f(x, y):
#  return (x ** 2 + y ** 2 > 128) or (y < -x + a)
#
# s = []
# for a in range(0, 200):
#     if all((f(x, y)) == 1 for x in range(0, 200) for y in range(0, 200)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       17


#       № 16
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 3
#     if n > 1:
#         f[n] = 3 * n + 2 * f[n - 1]
# print(f[2024] - 4 * f[2022])

#       Программа выведет:
#       18210


#       № 19 - 21
# def f(x, m):
#     if x >= 223: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 4, m - 1), f(x * 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 223) if f(s, 2)])

#       Программа выведет:
#       [74]

# print([s for s in range(1, 223) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [70, 73]

# print(min([s for s in range(1, 223) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       69


#       № 23
# def f(x, y):
#     if x > y or x == 18: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x + 4, y) + f(x * 2, y)
# print(f(4, 11) * f(11, 28))

#       Программа выведет:
#       483

