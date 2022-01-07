class Pegawai:
    honor_per_jam = 30000

    def __init__(self, nama, jumlah_jam):
        self.nama = nama
        self.jumlah_jam = jumlah_jam

    def honor(self):
        return f"{self.honor_per_jam * self.jumlah_jam}"


print(Pegawai('asnur', 6).honor())
