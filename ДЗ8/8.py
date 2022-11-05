#1.  Частина рядка(Easy: 0.3 point)
str = str(input().lower())
str_1 = str[:str.find("h")]
str_2 = str[str.find("h"):str.rfind("h") + 1:]
str_3 = str[str.rfind("h") + 1:]
print(str_1 + str_2[::-1] + str_3)


#2. Рядки та списки(Easy: 0.5 point)
def Count(str):
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
        elif str[i].isdigit():
            number += 1
        else:
            special += 1
    print([upper, lower, number, special])
str = "//LLOOab cde67890"
Count(str)


#3. Рядки та списки (Easy: 0.5 point )
list_num = []
for i in 'wfuhw312mjs19sj1d04':
    try:
        num = int(i)
        list_num.append(num)
    except ValueError:
        continue
print(list_num)
list_num = []
for i in 'wfuhw312mjs19sj1d04':
    try:
        num = int(i)
        list_num.append(num)
    except ValueError:
        continue
print(list_num)


#4. Функції та рядки (Easy: 0.5 point)
def probel(str_1):
    space = str_1.count(' ')
    rep_1 = str_1.replace(" ", "", space - 1)
    return  rep_1
str_1 = input('Введите строку')
print(probel(str_1))


#6. Словники. (Middle: 1 point)
dict = {
    'Київ': "Украина",
    'Берлін': "Німеччина",
    'Варшава': "Польща",
    'Париж': "Франція",
    'Лондон': "Англія",
    'Рим': ,
    'Стокгольм':
    'Гельсінки': "Фінляндія",
    'Рига': "Латвія",
    'Мадрид': "Іспанія",
}
while ansewer := dict.get(input(), "На жаль це не столиця"):
    print(ansewer)


#7. Перетворення словників (Middle: 1 point)
n = int(input())
ld = dict()
for i in range(n):
    ew, lw = input().split(" : ")
lws = lw.split(", ")
for w in lws:
    if w in ld:
        ld[w].append(ew)
    else:
        ld[w] = [ew]
print(ld)


#8. Рядкові паттерни (Middle*: 1.5 point)
def computeLPSArray(string, M, lps):
    length = 0
    i = 1
    lps[0] = 0
    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
def isRepeat(string):
    n = len(string)
    lps = [0] * n
    computeLPSArray(string, n, lps)
    length = lps[n - 1]
    if length > 0 and n % (n - length) == 0:
        return True
    else:
        False
txt = ["ababab"]
n = len(txt)
for i in range(n):
    if isRepeat(txt[i]):
        print(True)
    else:
        print(False)


#9. Дужки та рядки (Middle**: 1.7 point)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i!= dict[a]:
                    return False
        return stack == []


#10. Файли та рядки (Hard: 2.5 point)
def long_word_in_file(file_name: str) -> tuple:
    with open(file=file_name) as file:
        text = file.read()
        lst = text.split()
        long_word = max(lst, key=len)
        return long_word, text
def write_file_txt(list_text: str):
    with open('file_1.txt', "w", encoding="utf-8") as file:
        file.write(list_text)
if __name__ == '__main__':
    name_file = 'file_1.txt'
    word = long_word_in_file(name_file)
    count_letter(word[0])
    print(f'найдовше слово: {word[0]}')