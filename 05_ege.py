#          Тип 5 №


    #  29113 РЕШУ ЕГЭ
# for n in range(128, 256):
#     s = bin(n)[2:]
#     s = s.replace('1', '*')
#     s = s.replace('0', '1')
#     s = s.replace('*', '0')
#     r = int(s, 2)
#     if n - r == 185:
#         print(n)

#       Программа выведет:
#           220


    #  18618 РЕШУ ЕГЭ
# for n in range(100, 0, -1):
#     s = bin(n)[2:]
#     s = str(s)
#     s = s[::-1]
#     s = s[s.find('1'):]
#     r = int(s, 2)
#     if r == 11:
#         print(n)
#         break

#       Программа выведет:
#           56

