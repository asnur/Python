# fibonaci Iterasi
def fibonacci(x):
    bil1 = 1
    bil2 = 1
    print("|", bil1, end=" | ")
    for i in range(1, x):
        print(bil2, end=" | ")
        if ((i+1) % 5 == 0):
            print()
            print("| ", end="")
        c = bil2
        bil2 = bil2 + bil1
        bil1 = c


print("fungsi untuk menampilkan deret fibonacci sebanyak x buah")
x = int(input("masukkan x:"))
fibonacci(x)
