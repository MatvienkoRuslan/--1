years = int (input ("Введіть рік:"))
if years % 4 == 0 and years % 100 != 0:
    print('YES')
elif years % 400 == 0:
    print('YES')
else:
    print ('NO')