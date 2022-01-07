# fungsi Cari Biner

def cari_biner(data, elem):

    low = 0
    high = len(data) - 1

    while low <= high:

        middle = (low + high)//2

        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1


data = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
elem = 7

print(cari_biner(data, elem))
