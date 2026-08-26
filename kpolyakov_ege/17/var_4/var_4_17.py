#       Вариант № 4.


#       № 17
#  (№ 7683)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
# f = open('17-411.txt')
# s = [int(s) for s in f]
# # print(s)  #  Проверка на корректный поток чисел из файла 17.txt
# k = 0
# w = []
# mn = []
# mx = []
# for i in range(len(s)):
#     if s[i] % 3 == 0:
#         mn.append(s[i])
#     if s[i] % 10 == 3:
#         mx.append(s[i])
# for i in range(len(s) - 1):
#     if ((min(mn) <= s[i] <= max(mx)) and (s[i + 1] < min(mn) or s[i + 1] > max(mx))):
#         k += 1
#         w.append(s[i] ** 2 + s[i + 1] ** 2)
# print(k, min(w))

#       Программа выведет:
#       24 10309

