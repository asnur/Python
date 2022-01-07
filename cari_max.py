# Fungsi Cari Max
def cari_max(arr):

    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr[len(arr) - 1]


bilangan = [10, 2, 9]
print(cari_max(bilangan))
