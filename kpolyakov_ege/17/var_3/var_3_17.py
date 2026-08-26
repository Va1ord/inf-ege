#       Вариант № 3.


#       № 17
#  (№ 7684)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17-411.txt')
# s = [int(x) for x in f]
# # print(s)  #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# m = []
# for i in range(len(s)):
#     if s[i] % 10 == 1:
#         m.append(s[i])
# mx = max(m)
# for i in range(len(s) - 3):
#     k2 = 0
#     if s[i] < mx and s[i + 1] < mx and s[i + 2] < mx and s[i + 3] < mx:
#         if s[i] % 2 == 0:
#             k2 += 1
#         if s[i + 1] % 2 == 0:
#             k2 += 1
#         if s[i + 2] % 2 == 0:
#             k2 += 1
#         if s[i + 3] % 2 == 0:
#             k2 += 1
#         if k2 % 2 != 0:
#             k += 1
#             w.append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
# print(k, min(w))

#       Программа выведет:
#       117 559
