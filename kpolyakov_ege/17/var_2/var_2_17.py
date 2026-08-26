#       Вариант № 2.


#       № 17
#  (№ 7685)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# from math import *
# f = open('17-411.txt')
# s = [int(x) for x in f]
# # print(s)  #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s) - 1):
#     w.append(gcd(s[i], s[i + 1]))
# m = sorted(set(w))
# for i in range(len(m)):
#     if m[i] in w:
#         k = w.count(m[i])
# sm = []
# for i in range(len(s) - 1):
#     if gcd(s[i], s[i + 1]) == 17:
#         sm.append(s[i] + s[i + 1])
# print(max(sm))

#       Программа выведет:
#       1649

