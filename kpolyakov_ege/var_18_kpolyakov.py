#       Вариант № 18.


#       № 2
#  (№ 6586)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x or y) == (y <= z)) or w
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 0 0
#       0 0 1 0
#       0 1 0 0
#       1 1 0 0


#       № 6
#  (№ 6712) (ЕГЭ-2023)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# lt(90)
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(18 * m)
#     rt(90)
# up()
# fd(5 * m)
# rt(90)
# fd(7 * m)
# lt(90)
# down()
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(7 * m)
#     rt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 12
#  (№ 5993)
for n in range(1, 100):
    s = '>2' + n * '12' + '<'
    while '>2<' not in s:
        s = s.replace('>1', '>2', 1)
        s = s.replace('12<', '1<2', 1)
        s = s.replace('>21', '1>', 1)
        s = s.replace('1<', '<2', 1)
    if (s.count('1') + s.count('2') * 2) > 103:
        print(n)
        break

#       Программа выведет:
#



#       № 16
#  (№ 6755) (ЕГЭ-2023)
# f = {}
# for n in range(2025):
#     if n < 7:
#         f[n] = 7
#     if n >= 7:
#         f[n] = n + 1 + f[n - 2]
# print(f[2024] - f[2020])

#       Программа выведет:
#       4048


#       № 19 - 21
#  (№ 6389)
# def f(x, m):
#     if x >= 73: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 3, m - 1), f(x * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print(min([s for s in range(1, 73) if f(s, 2)]))

#       Программа выведет:
#       36

# print([s for s in range(1, 73) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [18, 33, 35]

# print([s for s in range(1, 73) if not f(s, 2) and f(s, 4)])

#       Программа выведет:
#       [32, 34]


#       № 23
#  (№ 7102)
# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     return f(x - 3, y) + f(x // 3, y) + f(x - 2, y)
# print(f(43, 21) * f(21, 15) * f(15, 13))

#       Программа выведет:
#       400

