def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(bubble_sort([34,87,1,56,90]))

def binary_search(list, val):
    n = len(list)
    left, right = 0, n - 1
    while left <= right:
        middle = (left + right) // 2
        if list[middle] == val:
            print("Element found")
            return middle
        elif list[middle] > val:
            right = middle - 1
        else:
            left = middle + 1
    print("Element not found")
    return -1

print(binary_search([27,89,90,1,4,6,5,7,23],7 ))