x = input()[:15]
y = len(x) // 2
print(x[y:-3] + x[-3:].upper() + x[:y])
