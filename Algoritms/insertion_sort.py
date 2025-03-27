def inserion_sort(arr):
    for i in range(1,len(arr)): # her yerini arayan elemanı gezen döngü
        key = arr[i] #elemanın değerini alıyoruz.
        j = i-1 # kendinden önceki sıralı listeye bakacağı için -1 yapıyoruz.
        while j >= 0 and key < arr[j]: # ya liste başına ulaşana kadar ya da key değeri gireceği aralığı bulduğunda son bulacak.(key arr[j] den büyükse orası doğru yerdir.)
            arr[j+1] = arr[j] #elemanları bir ileri alıyor yani key e yer açıyor misal 4.indexteki elemanı 5 e aldı sonra 3 ü 4 te filn.
            j -= 1 # bir önceki eleman için kontrol yapacak gerekirse bi ileri kaydırır.
        arr[j+1] = key # key değeri gereken aralığı bulduğunda yerine yerleşir j+1 olmasının sebei key > arr[j] durumunda j den büyükse j+1 olmalıdır.
    return arr #array geri döner.