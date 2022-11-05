list_1 = [1,10,22,66,26,2,7,25,9,55]
#A Виведіть усі елементи списку з парними індексами.
for el in range(0,len(list_1)):
    if el % 2 == 0:
        print(list_1[el])
    else:
        continue
#B Знайти суму елементів всього списку.
print(sum(list_1))
#C Знайти суму парних елементів списку та окремо непарних елементів списку.
print (sum([0 if x % 2 != 0 else x for x in list_1]))
print (sum([0 if x % 2 == 0 else x for x in list_1]))
#Виведіть значення найбільшого елемента у списку, а потім індекс цього елемента у списку.
#Якщо найбільших елементів кілька, виведіть індекс першого з них.
index_of_max = 0
for i in range(1, len(list_1)):
    if list_1[i] > list_1[index_of_max]:
        index_of_max = i
print(list_1[index_of_max], index_of_max)
