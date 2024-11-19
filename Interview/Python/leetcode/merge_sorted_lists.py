list1 = [1,2,4,10]
list2 = [1,3,4,6,7,9]

def merge_lists(list1, list2):
    merged_list = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            merged_list.append(list1[p1])
            p1 += 1
            if p1 == len(list1):
                merged_list.extend(list2[p2:])
                break
        else:
            merged_list.append(list2[p2])
            p2 += 1
            if p2 == len(list2):
                merged_list.extend(list1[p1:])
                break
    return merged_list

print(merge_lists(list1, list2))
