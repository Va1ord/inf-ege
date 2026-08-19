#          Тип 8 №


#  7667 РЕШУ ЕГЭ
# from itertools import *
# k = 0
# for x in product(sorted('ЕГЭ'), repeat=5):
#     s = "".join(x)
#     if s[0] in 'ЕЭ':
#         k += 1
# print(k)

#       Программа выведет:
#           162


#  3193 РЕШУ ЕГЭ
# from itertools import *
# words = list(product(sorted('ОАУ'), repeat=5))
# print(*words[209])

#       Программа выведет:
#           У О У А У


#  79721 РЕШУ ЕГЭ
# from itertools import *
# k = 0
# for x in permutations('0123456789', 4):
#     s = ''.join(x)
#     if s[0] != '0':
#         s = s.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
#         s = s.replace('1', '3').replace('5', '3').replace('7', '3').replace('9', '3')
#         if '22' not in s and '33' not in s:
#             k += 1
# print(k)

#       Программа выведет:
#           720

