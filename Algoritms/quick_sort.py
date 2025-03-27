def partition(arr):
    i,J =0
    pivot = arr[0]
    for j in range(len(arr)): # pivotla karşılaştırmak için elemanlar gezilir.
        if arr[j] < pivot:  #pivottan küçükse solunda yer almalıdır yani yeri değişmelidir.
            arr[j] , arr[i] = arr[i], arr[j] #i değeri en son değişen elemanın indexini tutar. o yüzden j ile i değişir.
            i += 1 # i yeni değer değişimleri için bir artar.
    arr[i], arr[0] = arr[0], arr[i] #pivot ile i nin son değeri değişir bu şekilde array işlemi biter pivot ortada yer alır.
    return arr

def quickSort(arr,start,end):
    if start < end:
        pivot = partition(arr)
        quickSort(arr,start,pivot-1)
        quickSort(arr,pivot+1,end)
    return arr

