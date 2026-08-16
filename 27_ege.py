# a = [0.543, 1.123]   распаковка
# x1, y1= a[0], a[1]
# print(a)
# print(x1, y1)

#  Здесь представлен тип задания из ЕГЭ 2025 года

def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1-y2)**2) ** 0.5

def centr(cl):
    mins = 10 ** 10  # c = [0, 0]
    for t1 in cl:
        s = 0
        x1, y1 = t1
        for t2 in cl:
            x2, y2 = t2
            s += dist(x1, y1, x2, y2)
        if s < mins:
            mins = s
            c = t1
    return c

f = open('27_1A.txt')
cl1 = []
cl2 = []
for s in f:
    s1 = s.replace(',', '.').split()
    t = [float(x) for x in s1]
    x, y = t
    if y > 15:
        cl1.append(t)
    else:
        cl2.append(t)

# print(cl1[:5])  # матрица (список списков)

x1, y1 = centr(cl1)
x2, y2 = centr(cl2)
print(int((x1 + x2) / 2 * 10000), int((y1 + y2) / 2 * 10000))