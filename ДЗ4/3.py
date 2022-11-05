list=[32,43,1,3,4,5,34,5,1,7,10,34,17,11]
num = []
num2 = []
k=1
for i in range(len(list)):
    if i % 5 == 0:
        if k % 2 == 0:
            num = sorted(list[i:i + 5],
reverse=True)
            num2.extend(num)
        else:
            num = sorted(list[i:i + 5],
reverse = False)
            num2.extend(num)
    k += 1
print(num2)