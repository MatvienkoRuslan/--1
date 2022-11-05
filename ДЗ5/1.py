list_sort = [1, 10, 9, 4, 5, 7, 2, 0]
def sortex(list, a, b):
    num = []
    print(f"list before: {list}")
    num = sorted(list[a:b])
    list_sort_1 = []
    list_sort_1.extend(list[0:a])
    list_sort_1.extend(num)
    list_sort_2 = []
    list_sort_2.extend(list[b:])
    list_sort_1.extend(list_sort_2)
    print(list_sort_1)
sortex(list_sort, 2, 6)