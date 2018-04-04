import texttable as tt
import getpass


def menu():
    print("===================================================")
    print("\n\t---pilihan---")
    print("\t1.penilaian mahasiswa")
    print("\t2.pembayaran mahasiswa")

    pilih = input("\n\tsilakan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2" :
        pembayaran()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nkembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    if tanya == "t":
        exit
    else:
        print ("\n\tsalah input...........!!!")

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []

    x = [[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == 'y'):
        nama.append(input("Masukkan Nama: "))
        nim.append(input("Masukkan Nim: "))
        tugas = int(input("Nilai Tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("Nilai UTS: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("Nilai UAS: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("Tambah data [y/t]?  ")


    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header(['No','Nama','Nim','Nilai Tugas', 'Nilai UTS', 'Nilai UAS','Nilai Akhir'])
    print (tab.draw())

def pembayaran():
    print("\n=====================================================")
    nama = input("\nMasukan Nama : ")
    nim = input("\nMasukan Nim : ")
    semester = input("\nMasukan semester saat ini : ")
    print("\n\t---pilihan pembayaran---")
    print("\t1. pembayaran SPP")
    print("\t2. pembayaran UTS")
    print("\t3. pembayaran UAS")
    print("\t4. pembayaran SPP & UTS")
    print("\t2. pembayaran SPP & UAS")
    pilih = input("\n\tsilakan pilih : ")
    if pilih == "1":
        spp ()
    elif pilih == "2":
        uts ()
    elif pilih == "3" :
        uas ()
    elif pilih == "4" :
        spp_uts ()
    elif pilih == "5" :
        spp_uas ()
    else:
        exit
        tanya()

def spp():
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 500000 * bulan
    print("========================================================")
    print("\ttotal bayar spp Rp.500000 *" ,bulan, " = Rp. ", total)

def uas():
    matkul = int(input("\n\tjumlah mata kuliah = "))
    matkul = float(matkul)
    byr_uas = 50000 * matkul
    print("========================================================")
    print("\ttotal yang harus di bayar Rp.50000 * ",matkul," = Rp. ",total)

def uts():
    matkul_uts = int(input("\n\tjumlah mata kuliah = "))
    matkul_uts = float(matkul_uts)
    total = 50000 * matkul_uts
    print("========================================================")
    print("\ttotal yang harus dibayar Rp. 50000 * ",matkul_uts," = Rp. ",total)

def spp_uas():
   bulan = int(input("\n\tjumlah bulan yang dibayar = "))
   matkul = int(input("\n\jumlah mata kuliah = "))
   matkul =float(matkul)
   bulan =float(bulan)
   total_spp = 500000 * bulan
   byr_uas = 50000 * matkul
   total = total_spp + byr_uas + 5000
   print ("\ttotal bayar spp Rp. 500000 * ",bulan," = Rp. ", total_spp)
   print ("\ttotal bayar uas Rp.50000 * ",matkul," = Rp. ", byr_uas)
   print ("\tbiaya tambahan server sebesar Rp. 5000")
   print("=======================================================")
   print("\ttotal yang harus dibayar",total)


def spp_uts():
   bulan = int(input("\n\tjumlah bulan yang di bayar = "))
   matkul = int(input("\n\tjumlah mata kuliah = "))
   bulan = float(bulan)
   matkul = float(matkul)
   total_spp = 500000 * bulan
   byr_uts = 50000 * matkul
   total = total_spp + byr_uts + 5000
   print("\ttotal bayar spp Rp.5000000 * ",bulan," = Rp.",total_spp)
   print("\ttotal bayar uts Rp.50000 * ",matkul," = Rp.",byr_uts)
   print("\tbiaya tambahan server sebesar Rp.5000")
   print("======================================================")
   print("\ttotal yang harus dibayar", total)


username = input("\nusername : ")
password = getpass.getpass()
print("========================================================")

if username == "nida" and password == "1796" :
    menu()

else:
    print ("maaf password atau username ini salah..............!!!")
    
