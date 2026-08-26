#       Вариант № 16.


#       № 2
#  (№ 6687) (ЕГЭ-2023)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and y) or (y == z) or w
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       0 1 0 0
#       1 0 1 0


#       № 5
#  (№ 6999)
# for n in range(1 ,1000):
#     s = bin(n)[2:]
#     ind = s.rfind('0')
#     s = s[:ind] + s[:2] + s[ind + 1:]
#     s = s[::-1]
#     r = int(s, 2)
#     if r == 123:
#         print(n)
#         break

#       Программа выведет:
#       47


#       № 6
#  (№ 6812) (ЕГЭ-2023)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# rt(90)
# for i in range(3):
#     rt(45)
#     fd(10 * m)
#     rt(45)
# rt(315)
# fd(10 * m)
# for i in range(2):
#     rt(90)
#     fd(10 * m)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 12
#  (№ 6234) (PRO100 ЕГЭ)
# w = []
# for n in range(1, 1000):
#     s = '>' + 39 * '0' + n * '1' + 39 * '2'
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     sm = s.count('1') + s.count('2') * 2
#     for i in range(1, 100):
#         if sm == i ** 2:
#             w.append(n)
# print(min(w))

#       Программа выведет:
#       1


#       № 14
#  (№ 7475) (ЕГЭ-2024)
# mx_x = 0  #  Максимальный x
# for x in range(1, 7051):
#     n = 5 ** 100 - x
#     k = 0
#     while n > 0:
#         if n % 5 == 0:
#             k += 1
#         n //= 5
#     if k == 3:
#         mx_x = x
# print(mx_x)

#       Программа выведет:
#       7000


#       № 19 - 21
#  (№ 6557)
def f(x, m):
    if x >= 100: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 7, m - 1), f(x * 2, m - 1)]
    if m % 2 != 0:
        return any(h)
    else:
        return any(h)  #  В 21 и 22 задании поменяйте на all(h)

print(max([s for s in range(1, 100) if f(s, 2)]))

#       Программа выведет:
#       92

print([s for s in range(1, 100) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#

print(min([s for s in range(1, 100) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       29


#       № 23
#  (№ 7116)
# def f(x, y):
#     if x < y or (x == 33 and x == 31): return 0
#     if x == y: return 1
#     return f(x - 3, y) + f(x - 4, y)
# print(f(44, 19))

#       Программа выведет:
#       43

