def merge_sort(list1):
    if len(list1) > 1:  # this will be the condition for dividing
        mid = len(list1) // 2
        left_list = list1[:mid]  # split list from beginning to mid not include mid ele
        right_list = list1[mid:]  # split list from mid to end
        merge_sort(left_list)
        merge_sort(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                # if left_list[i] > right_list[j]:  # if i want descending order ele
                list1[k] = left_list[i]  # this condition will be merging
                i += 1
                k += 1
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1
        while i < len(left_list):  # here 2 cond check any value are left out or not
            list1[k] = left_list[i]  # this is check whether any value left in left sublist or not
            i = i + 1
            k = k + 1

        while j < len(right_list):  # this is check whether any value left in right sublist or not
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1  # 12,2,4,5,6


num = int(input('how many elements you want in list:'))
list1 = [int(input()) for x in range(num)]
merge_sort(list1)
print('sorted list', list1)



