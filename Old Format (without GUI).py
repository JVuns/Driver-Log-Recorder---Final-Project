from datetime import date
import os
import os.path
today = date.today()

menu = "Menu_1"
def initializer():
    path = "C:/Users/jevon/Documents/Coaloc/"
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

class Karyawan:
    def __init__(self,karyawan,upahdasar,jenis_m,jalur,tanggal,route):
        self.karyawan = karyawan
        self.upahdasar = upahdasar
        self.jenis_m = jenis_m
        self.jalur = jalur
        self.tanggal = tanggal
        self.route = route

    # Method start here

    def perhitungan(self):
        if self.jenis_m != "":
            # path = "C:/Users/jevon/Documents/Coaloc/Data_kendaraan/"
            # filename = os.path.join(path + self.jenis_m)
            # with open(filename, mode="r", encoding="utf-8") as rdata:
            # kredit_k = rdata.readline
            return(float(self.upahdasar))
        else:
            return(f"jenis {self.jenis_m} tidak ada")
            

    def rekam(self, nama):
        path = str("C:/Users/jevon/Documents/Coaloc/Data_karyawan/")
        try:
            os.mkdir(path)
            pass
        except FileExistsError:
            filename = os.path.join(path + nama + ".txt")
        with open(filename,mode = "a", encoding = "utf-8") as fdata:
            fdata.write("Tanggal: "+ self.tanggal + "\t" + 
            "kredit/rute: "+str(self.perhitungan()) + "\t" +
            "retasi: " +str(self.route)+ "\t"
            "total kredit: " +str(int(self.perhitungan())*int(self.route))+ "\n")
            print("data terekam")
            print("data dir: " + filename)

def kendaraan_inp():
    dir_ = "C:/Users/jevon/Documents/Coaloc/Data_kendaraan/"
    try:
        os.mkdir(dir_)
    except FileExistsError:
        pass
    jenis_m = str(input("Nama kendaraan: "))
    filename = os.path.join(dir_ + jenis_m + ".txt")
    if os.path.isfile(filename):
        print(f"Data {jenis_m} sudah ada")
        opsi = str(input("(Hapus / rubah / Keluar)\n"))
        if opsi in ["hapus","h","Hapus"]:
            opsi = str(input(f"Hapus {jenis_m} ?\n(Y/N)"))
            if opsi in ["ya","y","Ya","Y"]:
                os.remove(filename)
            elif opsi in ["N","n","no","No"]:
                pass
            else:
                print("Opsi tidak ada")
        elif opsi in ["rubah","r"]:
            with open(filename, mode="w", encoding="utf-8") as fdata:
                nama_kendaraan = str(input("Nama kendaraan: "))
                kredit_kendaraan = str(input("Harga/ret: "))
                opsi = str(input("Simpan rubahan? \n(Y/N)\n"))
                if opsi in ["ya","y","Ya","Y"]:
                    fdata.write("Nama kendaraan: " + nama_kendaraan +"\t"
                    "Harga/ret: " + kredit_kendaraan + "\n")
                elif opsi in ["N","n","no","No"]:
                    pass
                else:
                    print("Opsi tidak ada")
        elif opsi in ["keluar","k","K","Keluar"]:
            pass
    else:
        with open(filename, mode="w", encoding="utf-8") as fdata:
                kredit_kendaraan = str(input("Harga/ret: "))
                opsi = str(input("Simpan data? \n(Y/N)\n"))
                if opsi in ["ya","y","Ya","Y"]:
                    fdata.write("Nama kendaraan: " + jenis_m +"\t"
                    "Harga/ret: " + kredit_kendaraan + "\n")
                    print(f"data {jenis_m} telah disimpan")
                elif opsi in ["N","n","no","No"]:
                    pass
                else:
                    print("Opsi tidak ada")

def hapuskar():
    dir_ = "C:/Users/jevon/Documents/Coaloc/Data_karyawan/"
    nama = input("Nama karyawan: ")
    filename = os.path.join(dir_ + nama + ".txt")
    if os.path.isfile(filename):
        opsi = str(input(f"Hapus data {nama}?\n(Y/N)\n"))
        if opsi in ["y","Y","Ya","YA"]:
            os.remove(filename)
            print(f"Data {nama} dihapus")
        else:
            pass
    else:
        print(f"Data {nama} tidak ada")

def hapusken():
    dir_ = "C:/Users/jevon/Documents/Coaloc/Data_kendaraan/"
    nama = input("Nama Kendaraan: ")
    filename = os.path.join(dir_ + nama + ".txt")
    if os.path.isfile(filename):
        opsi = input(f"Hapus data {nama}?\n(Y,N)\n")
        if opsi in ["y","Y","ya","YA"]:
            os.remove(filename)
            print(f"Data {nama} dihapus")
        else:
            pass
    else: 
        print(f"Data {nama} tidak ada")
        
def baca():
    nama = input("nama karyawan: ")
    def_dir = "C:/Users/jevon/Documents/Coaloc/Data_karyawan/"
    filename = os.path.join(def_dir + nama + ".txt")
    try:
        with open(filename, mode="r", encoding = "utf-8") as rdata:
            for data in rdata:
                print(data)
            sub_pilihan = str(input("pilihan (Totalkan, keluar): "))
            if sub_pilihan == "totalkan" or sub_pilihan == "t":
                pass #total()
                os.remove(filename)
            elif sub_pilihan == "keluar" or sub_pilihan == "k": 
                pass #pass
    except FileNotFoundError:
        print("data karyawan tidak ada")


def inputs():
    nama = input("nama: ")
    upahdasar = input("upah dasar: ")
    jenis_m= input("jenis mobil: ")
    jalur = input("jalur: ")
    tanggal = str(today.strftime("%d/%m/%Y"))
    route = int(input("banyak rute: "))
    data = Karyawan(nama, upahdasar, jenis_m, jalur, tanggal, route)
    data.rekam(nama)


while menu == "Menu_1":
    pilihan = str(input("pilihan (penambahan data / pembacaan data / hapus data / keluar): "))
    print()
    if pilihan == "penambahan data" or pilihan == "tambah":
        menu = "Menu_sub1"
    elif pilihan == "pembacaan data" or pilihan == "baca":
        baca()
    elif pilihan in ["hapus", "hapus data", "h"]:
        opsi = str(input("Hapus data: kendaraan / karyawan\n"))
        if opsi in ["kendaraan","ke"]:
            hapusken()
        elif opsi in ["karyawan","ka"]:
            hapuskar()
    elif pilihan == "keluar" or pilihan == "keluar":
        exit()
    else: 
        print("pilihan tidak valid")    
    while menu == "Menu_sub1":
        pil_data = str(input("pilihan (data karyawan / data kendaraan) :"))
        if pil_data in ["data karyawan", "karyawan"]:
            inputs()
        elif pil_data in ["data kendaraan","kendaraan"]:
            kendaraan_inp()
        elif pil_data in ["k","K","Keluar","keluar"]:
            menu == "Menu_1"
        else:
            print("Pilihan tidak valid")


