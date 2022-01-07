import requests
from tabulate import tabulate
from os import system

class Provinsi:
    total_data = 10
    url = "https://dev.farizdotid.com/api/daerahindonesia/provinsi"
    data = []

    def dataProvinsi(self, order = "ASC", page=1):
        header = ['No', 'Nama Provinsi']
        response = requests.get(self.url).json()['provinsi']
        for i in range(len(response)):
            self.data.append([i+1, response[i]['nama']])
        start = self.total_data * (page -1)
        self.data = self.data[start:start+self.total_data]
        self.data = sorted(self.data, reverse=True if order == "DESC" else False)
        print(tabulate(self.data, header, tablefmt="github"))

    def preview(self):
        system('cls')
        print("="*16)
        print("DATA PROVINSI")
        print("="*16)
        print()

        order = input("Urutan Data ASC/DESC : ")
        page = int(input("Halaman : "))
        # data = Provinsi(order, page)

        self.dataProvinsi(order, page)

        again = input("Lihat Data Lainnya (Y/N) : ").upper()

        if again == "Y":
            self.preview()


view = Provinsi()

view.preview()