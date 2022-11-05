fizz= int(input('fizz'))
buzz= int(input('buzz'))
noise = int(input('Введіть кількість чисел'))

for x in range(1, noise+1):
    if x % fizz== 0 and x % buzz== 0:
        print("FB",end=' ')
    elif x % fizz== 0:
        print("F",end=' ')
    elif x % buzz== 0:
        print("B",end=' ')
    else:
        print(x,end=' ')
