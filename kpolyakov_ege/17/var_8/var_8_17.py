#       Вариант № 8.


#       № 17
#  (№ 7564) (ЕГЭ-2024)
#  Перед выполнением данного задания необходимо скачать файл с оффициального сайта Полякова
f = open('17-409.txt')
s = [int(x) for x in f]
# print(s)   #  Проверка на корректный поток чисел из файла 17.txt
k = 0
w = []
m = []
for i in range(len(s)):
    if abs(s[i]) % 10 == 7 and 999 < abs(s[i]) < 10000:
        m.append(s[i])
mx = max(m)
for i in range(len(s) - 2):
    if ((s[i] % 10 == 7 and 999 < abs(s[i]) < 10000) and (s[i + 1] % 10 == 7 and 999 < abs(s[i + 1]) < 10000)) or \
        ((s[i + 1] % 10 == 7 and 999 < abs(s[i + 1]) < 10000) and (s[i + 2] % 10 == 7 and 999 < abs(s[i + 2]) < 10000)) or \
          ((s[i] % 10 == 7 and 999 < abs(s[i]) < 10000) and (s[i + 2] % 10 == 7 and 999 < abs(s[i + 2]) < 10000)):
        if (s[i] + s[i + 1] + s[i + 2]) > mx:
            k += 1
            w.append(s[i] + s[i + 1] + s[i + 2])
print(k, max(w))

