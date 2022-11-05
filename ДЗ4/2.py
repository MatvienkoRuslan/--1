file1 = open('file_1.txt', 'r')
count = 0

while True:
    count += 1
    line = file1.readline()
    if not line:
        break
for i in line.strip():
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
            print('Fizz')
    elif i%5==0:
            print('Buzz')
    else:
        print(i)