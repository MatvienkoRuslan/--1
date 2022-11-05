str = input()[:10]
s = str[-3:].lower()
middle = len(str[:-3]) // 2
str = str[:-3]
print(str[:middle] + s + str[middle:])