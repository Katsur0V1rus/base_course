n = int(input('Введите элементов прогрессии:'))
b_first = int(input('Введите первый элеменгт прогрессии:'))
q = int(input('Введите знаменатель прогрессии:'))
print(b_first)
b_prev = b_first

summa = b_prev
for i in range(1,n):
    b_cur = b_prev*q
    print(b_cur)

summa = summa + b_cur
b_prev = b_cur
print('Сумма элементов геометрической прогрессии =', summa)
