#       Вариант № 13.


#       № 2
#  (№ 6690)
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z, w)

#       Программа выведет:
#       x y z w
#       0 0 1 0
#       0 1 1 0
#       1 1 0 0


#       № 5
#  (№ 7055) (PRO100-ЕГЭ)
# def f(n):
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
#
# for n in range(1, 1000):
#     s = f(n)
#     if n % 2 == 0:
#         s = '1' + s + '00'
#     else:
#         s = s + f(sum([int(i) for i in s]))
#     r = int(s, 3)
#     if r > 168:
#         print(n)
#         break

#       Программа выведет:
#       10


#       № 6
#  (№ 6895)
# from turtle import *
# tracer(0)
# screensize(10000, 10000)
# m = 30
# x = 3
# lt(90)
# for i in range(4):
#     fd((3 * x) * m)
#     rt(90)
# up()
# fd(x * m)
# rt(90)
# fd(x * m)
# down()
# for i in range(4):
#     fd(x * m)
#     lt(90)
# up()
# for x in range(-90, 90):
#     for y in range(-90, 90):
#         goto(x * m, y * m)
#         dot(3, 'blue')
# done()


#       № 8
#  (№ 7252)
# from itertools import *
# k = 0
# for x in product(sorted('ПРИВЫЧКА'), repeat=5):
#     s = ''.join(x)
#     k += 1
#     if k % 5 != 0 and len(set(x)) == 5 and all(i not in x for i in 'ИЫА'):
#         print(k - k // 5)
#         break

#       Программа выведет:
#       4754


#       № 12
#  (№ 6520)
# for n in range(3, 100):
#     s = '3' + n * '7'
#     while '37' in s or '577' in s or '777' in s:
#         if '37' in s:
#             s = s.replace('37', '7', 1)
#         if '577' in s:
#             s = s.replace('577', '73', 1)
#         if '777' in s:
#             s = s.replace('777', '5', 1)
#     sm = sum([int(i) for i in s])
#     if sm >= 10 and sm % 2 != 0 and n % 2 != 0:
#         print(sm, n)

#       Программа выведет:
#       ...
#       13 97 - Ответ


#       № 14
#  (№ 7478) (ЕГЭ-2024)
# for x in range(8300, 10000):
#     n = 5 ** 100 - x
#     k = 0
#     while n > 0:
#         if n % 5 == 0:
#             k += 1
#         n //= 5
#     if k == 4:
#         print(x)
#         break

#       Программа выведет:
#       8750


#       № 15
#  (№ 6747) (ЕГЭ-2023)
# def f(x, y):
#     return (x < a) or (y < a) or (x + 2 * y > 50)
# s = []
# for a in range(0, 300):
#     if all(f(x, y) == 1 for x in range(0, 300) for y in range(0, 300)):
#         s.append(a)
# print(min(s))

#       Программа выведет:
#       17


#       № 17
#  (№ 7485) (ЕГЭ-2024)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17.txt')
# s = [int(x) for x in f]
# # print(s)   #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s)):
#     m.append(s[i])
# mn = min(m)
# for i in range(len(s) - 1):
#     if s[i] % 55 == mn or s[i + 1] % 55 == mn:
#         k += 1
#         w.append(s[i] + s[i + 1])
# print(k, min(w))

#       Программа выведет:
#       201 2942


#       № 19 - 21
#  (№ 6767) (ЕГЭ-2023)
# def f(x, m):
#     if x >= 88: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 1, m - 1), f(x + 4, m - 1), f(x * 3, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else:
#         return all(h)

# print([s for s in range(1, 88) if f(s, 2)])

#       Программа выведет:
#       [29]

# print([s for s in range(1, 88) if not f(s, 1) and f(s, 3)])

#       Программа выведет:
#       [25, 28]

# print(min([s for s in range(1, 88) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#       24


#       № 23
#  (№ 7206)
# def f(x, y):
#     if x > y or x == 15 or x == 35: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x * 2, y) + f(x ** 2, y)
# print(f(2, 20) * f(20, 60) * f(60, 100))

#       Программа выведет:
#       319

