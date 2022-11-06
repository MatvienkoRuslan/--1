st = (input('Введіть значення'))
flag = True;
for i in range(0, len(st) // 2):
    if (st[i] != st[len(st) - i - 1]):
        flag = False;
        break

if (flag):
    print("Ні");
else:
    print("Так");