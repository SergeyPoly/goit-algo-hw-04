from sort_alhorithms import merge

def merge_k_lists(lists):
    # Перший цикл повторюється до тих пір, поки у списку (змінна lists) не залишиться лише один елемент - потрібний результат
    while len(lists) > 1:
        merged_lists = []

        # Другий цикл почергово зливає два списки що знаходяться поруч (якщо їх кількість непарна, останній зливається з пустим списком) 
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge(list1, list2))

        # Результати злиття після відпрацювання другого циклу перезаписуються у змінну lists
        lists = merged_lists

    return lists[0] if lists else []


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)