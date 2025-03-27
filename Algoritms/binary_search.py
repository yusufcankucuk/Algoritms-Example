dummy_array = [80,90,47,59,12,15,23,21,33,56,78,99]
sorted_array = sorted(dummy_array)

def binary_search(arr,target,left,right):
    if left > right:
        return -1
    mid = (left+right)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,right)
    else:
        return binary_search(arr,target,left,mid-1)
    

print(sorted_array)
print(binary_search(sorted_array,59,0,len(sorted_array)-1))