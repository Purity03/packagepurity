def bubble_sort(items):
    length = len(items) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,length):
            if items[i] > items[i + 1]:
                 hold = items[i + 1]
                 items[i + 1] = items[i]
                 items[i] = hold
                 sorted = False
    return items


def merge_sort(items):

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    new_list = []
    while len(i1) > 0 and len(i2) > 0:
        if i1[0] < i2[0]:
            new_list.append(i1[0])
            i1.pop(0)
        else:
            new_list.append(i2[0])
            i2.pop(0)

    if len(i1) == 0:
        new_list = new_list + i2
    if len(i2) == 0:
        new_list = new_list + i1

    return new_list


def quick_sort(items):
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        initial = quick_sort(items[:i])
        last = quick_sort(items[i+1:])
        initial.append(items[i])
        return initial + last
