#       Вариант № 10.


#       № 2
#  (№ 6708) (ЕГЭ-2023)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (y <= x) and (not z) and w
#                 if f == 1:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 1
#       1 0 0 1
#       1 1 0 1


#       № 5
#  (№ 7386)
# def f(n):
#     s = ''
#     while n > 0:
#         s += str(n % 8)
#         n //= 8
#     return s[::-1]
#
# w = []
# for n in range(1, 1000):
#     s = f(n)
#     if sum([int(i) for i in s]) % 2 == 0:
#         s = s[0] + s + s[0]
#     else:
#         s = s + s[-1]
#     r = int(s, 8)
#     if r < 1100:
#         w.append(n)
# print(max(w))

#       Программа выведет:
#       136


#       № 6
#  (№ 7359)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(5):
#     rt(45)
#     fd(10 * m)
#     rt(45)
# for i in range(6):
#     fd(20 * m)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7397)
# from itertools import *
# k = 0
# w = []
# for x in product('АВР', repeat=7):
#     s = ''.join(x)
#     if s.count('А') == 3 and s.count('В') == 2 and s.count('Р') == 2:
#         k += 1
#         if s[0] == 'В' and 'ААА' in s and 'РР' not in s:
#             if k % 2 == 0:
#                 w.append(k)
# print(max(w))

#       Программа выведет:
#       146


#       № 12
#  (№ 6734) (ЕГЭ-2023)
# mx_sum = 0  #  Максимальная сумма строки
# for n in range(3, 10000):
#     s = '1' + n * '2'
#     while '12' in s or '322' in s or '222'  in s:
#         if '12' in s:
#             s = s.replace('12', '2', 1)
#         if '322' in s:
#             s = s.replace('322', '21', 1)
#         if '222' in s:
#             s = s.replace('222', '3', 1)
#     cur_sum = sum([int(i) for i in s])
#     if cur_sum >= mx_sum:
#         mx_sum = cur_sum
# print(mx_sum)

#       Программа выведет:
#       17


#       № 13
#  (№ 7471) (ЕГЭ-2024)
# from itertools import *
# k = 0
# for x in product('01', repeat=19):
#     s = ''.join(x)
#     if (8 + s.count('1')) % 2 != 0:
#         k += 1
# print(k)

#       Программа выведет:
#       262144


#       № 14
#  (№ 7557) (ЕГЭ-2024)
# for x in range(1, 1000):
#     n = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
#     k = 0
#     while n > 0:
#         if n % 6 == 0:
#             k += 1
#         n //= 6
#     if k == 202:
#         print(x)
#         break

#       Программа выведет:
#       216


#       № 15
#  (№ 7253)
# for a in range(1, 3000):
#     if all(((x & 2735 != 0) <= ((x & 1234 == 0) <= (x & a != 0)) for x in range(1, 3000))):
#         print(a)
#         break

#       Программа выведет:
#       2605


#       № 16
#  (№ 7388)
# f = {}
# for n in range(2025):
#     if n == 1:
#         f[n] = 6
#     if n > 1:
#         f[n] = 3 * n + 2 + f[n - 1]
# print(f[2024] - f[2020])

#       Программа выведет:
#       24278


#       № 19 - 21
#  (№ 6770)
# def f(x, m):
#     if x >= 82: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 2, m - 1), f(x + 4, m - 1), f(x * 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return any(h)  #  В 21 и 22 задании поменяйте на all(h)

# print(min([s for s in range(1, 82) if f(s, 2)]))

#       Программа выведет:
#       10

# print([s for s in range(1, 82) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [9, 22, 23, 24, 25]

# print(max([s for s in range(1, 82) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       21


#       № 23
