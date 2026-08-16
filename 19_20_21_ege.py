#          Тип 19, 20, 21 №


#  const x = Куча 1
#  const y = Куча 2
#  const m = Общий игровой счёт
#  const h = Варианты ходов
#  Задание 19 идёт вместе с номерами 20, 21. Их ещё называют "Теория игр"


#  73845 РЕШУ ЕГЭ
# def f(x, m):
#     if x <= 19: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x - 5, m - 1)]
#     if x % 2 == 0:
#         h.append(f(x // 2, m - 1))
#     if x % 3 == 0:
#         h.append(f(x // 3, m - 1))
#     if x % 2 != 0 and x % 3 != 0:
#         h.append(f(x + 1, m - 1))
#     if m % 2 != 0: return any(h)
#     else: return all(h)
# print(min([s for s in range(20, 100) if f(s, 2)]))

# #       Программа выведет:
# #           25

# #     20 Задание
# print([s for s in range(20, 100) if not f(s, 1) and f(s, 3)])

# #       Программа выведет:
# #           [40, 43, 46, 49, 50, 52, 55, 58, 61, 62, 70, 74, 75, 82, 87, 88, 93, 94]

# #     21 Задание
# print(min([s for s in range(20, 100) if not f(s, 2) and f(s, 4)]))

#       Программа выведет:
#           60



# def f(x, y, m):
#     if x + y >= 231: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(x + 2, y, m - 1), f(x, y + 2, m - 1), f(x * 2, y, m - 1), f(x, y * 2, m - 1)]
#     if m % 2 != 0:
#         return any(h)
#     else: return any(h)
# print([s for s in range(1, 214) if (17, s, 2)])

