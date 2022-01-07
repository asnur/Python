# faktorial iterasi
n = int(input('Masukkan nilai n: '))


def hitung_faktorial(n):
    hasil = 1
    if n > 2:
        for i in range(2, n+1):
            hasil *= i
        return hasil
    return 2


faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')
