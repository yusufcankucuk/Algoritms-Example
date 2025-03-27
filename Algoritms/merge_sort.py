def mergeSortedArray(arr1, arr2):
    result = []
    n1, n2 = 0, 0

    while n1 < len(arr1) and n2 < len(arr2):
        if arr1[n1] < arr2[n2]:
            result.append(arr1[n1])
            n1 += 1
        else:
            result.append(arr2[n2])
            n2 += 1

    while n1 < len(arr1):
        result.append(arr1[n1])
        n1 += 1

    while n2 < len(arr2):
        result.append(arr2[n2])
        n2 += 1

    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid]) # 0 dan mid e kadar.
    right = mergeSort(arr[mid:])#mid+1 den sona kadar.
    return mergeSortedArray(left, right)


