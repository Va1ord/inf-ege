#          Тип 23 №


#  15990 РЕШУ ЕГЭ
# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     return f(x + 2, y) + f(x * 2, y) + f(x + 3, y)
# print(f(2, 11) * f(11, 22))

#       Программа выведет:
#           100


#  70550 РЕШУ ЕГЭ
# def f(x, y):
#     if y > x: return 0
#     if x == y: return 1
#     return f(x - 2, y) + f(x // 2, y)
# print(f(38, 16) * f(16, 2))

#       Программа выведет:
#           36


#  13418 РЕШУ ЕГЭ
# def f(x, y):
#     if x > y or x == 26: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x * 2 + 1, y)
# print(f(1, 27))

#       Программа выведет:
#           13


#  15834 РЕШУ ЕГЭ
# def f(x, y):
#     if x > y or x == 31: return 0
#     if x == y: return 1
#     return f(x + 1, y) + f(x * 2, y)
# print(f(2, 15) * f(15, 35))

#       Программа выведет:
#           26

#  63039 РЕШУ ЕГЭ
# def f(x, y, k):
#     if x > y + 1: return 0
#     if x == y: return 1
#     else:
#         if k == 1:
#             return f(x * 2, y, k - 1) + f(x * 3, y, k - 1)
#         else:
#             return f(x - 1, y, k + 1) + f(x * 2, y, k) + f(x * 3, y, k)
# print(f(3, 20, 0))

#       Программа выведет:
#           4

