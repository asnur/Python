import datetime


class Orang:
    def __init__(self, nama, tgl_lahir):
        date = tgl_lahir.split("-")
        self.nama = nama
        self.tgl_lahir = datetime.datetime(
            int(date[0]), int(date[1]), int(date[2]))
        self.tahun_sekarang = datetime.datetime.now()

    def umur(self):
        return f"{self.tahun_sekarang.year - self.tgl_lahir.year}"


print(Orang('asnur', '2001-12-01').umur())
