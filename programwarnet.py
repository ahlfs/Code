import secrets
import string
pilihan = ""
pc = ""
harga = ""
tarif = int(90)
tarif2 = int(200)
tarif3 = int(300)
paket1 = int(500000)
paket2 = int(100000)
paket3 = int(250000)
paket4 = int(450000)
paketx = int(1)
no = string.digits
huruf = string.ascii_letters
gabung = no + huruf
panjang = 8
panjang2 = 17
order = ""
ref = ""
for i in range(panjang):
    order+= "" .join(secrets.choice(no))
for i in range(panjang):
    ref+= "" .join(secrets.choice(gabung))
print("==============================================")
print("                  WELCOME")
print("==============================================")

def start():
    print("================Daftar Menu===================")
    print("1. Sewa")
    print("2. Menginap")
    print("==============================================")
    pilihan = input("Masukan pilihan: ")
    if pilihan == "1":
        sewa()
    elif pilihan == "2":
        menginap()
    else:
        print("Silahkan masukan menu yang ada")
        start()
        
def sewa():
    global pilihan
    global harga
    global pc
    print("=======Silahakan Pilih Paket Pc=========")
    print("1. Paket Reguler (i3 gen 11300, 8GB RAM) Tarif per menit: Rp. ",tarif )
    print("2. Paket Premium (i5 gen 12500, 16GB RAM, GTX 1650) Tarif per menit: Rp. ",tarif2 )
    print("3. Paket Supreme (i9 gen 13900K,32GB RAM, RTX 3090 Ti) Tarif per menit: Rp. ",tarif3 )
    print("==============================================")
    print("4. Kembali Ke Menu")
    print("==============================================")
    
    pilihan = input("Masukan nomor paket: ")
    if pilihan == "1":
        jam = int(input("Masukan berapa menit kamu ingin menyewa: "))
        pc = input("Masukan nomor pc yang ingin di gunakan: ")
        harga = tarif * jam
        paymentsewa()
    elif pilihan == "2":
        jam = int(input("Masukan berapa menit kamu ingin menyewa: "))
        pc = input("Masukan nomor pc yang ingin di gunakan: ")
        harga = tarif2 * jam
        paymentsewa()
    elif pilihan == "3":
        jam = int(input("Masukan berapa menit kamu ingin menyewa: "))
        pc = input("Masukan nomor pc yang ingin di gunakan: ")
        harga = tarif3 * jam
        paymentsewa()
    elif pilihan == "4":
        start()
    
def menginap():
    global paketx
    global pilihan
    print("=======Silahakan Pilih Paket Menginap=========")
    print("1. Paket Satu Malam Rp. ", paket1)
    print("2. Paket Satu Hari Rp. ", paket2)
    print("3. Paket Tiga Hari Rp. ", paket3)
    print("4. Paket Satu Minggu Rp. ", paket4)
    print("==============================================")
    print("5. Kembali Ke Menu")
    print("==============================================")
    pilihan = input("Masukan Nomor Paket: ")
    if pilihan == "1":
        paketx = paketx * paket1
        jumlah = int(input("Berapa Jumlah Paket yang ingin dibeli : "))
        paketx = paketx * jumlah
        paymentinap()
    elif pilihan == "2":
        paketx = paketx * paket2
        jumlah = int(input("Berapa Jumlah Paket yang ingin dibeli : "))
        paketx = paketx * jumlah
        paymentinap()
    elif pilihan == "3":
        paketx = paketx * paket3
        jumlah = int(input("Berapa Jumlah Paket yang ingin dibeli : "))
        paketx = paketx * jumlah
        paymentinap()
    elif pilihan == "4":
        paketx = paketx * paket4
        jumlah = int(input("Berapa Jumlah Paket yang ingin dibeli : "))
        paketx = paketx * jumlah
        paymentinap()
    elif pilihan == "5":
        start()
    else:
        print("Silahkan Masukan Nomor Paket Yang Ada")
        menginap()
        
def paymentsewa():
    print("======Silahkan Pilih Metode Pembayaran========")
    print("1. Cash")
    print("2. Gopay")
    print("==============================================")
    print("3. Kembali")
    print("==============================================")
    pilihan = input("Pilih Metode Pembayaran : ")
    if pilihan == "1":
        uang = int(input("Uang Yang Diterima : "))
        if uang >= harga:
            balik = uang - harga
            print("================Nota Pembayaran===============")
            print("Pc no: " , pc)
            print("Harga yang perlu di bayar: Rp. ", harga)
            print("Uang Diterima : ", uang)
            print("Kembalian : ", balik)
            print("Metode Pembayaran : Cash")
            print("==============================================")
            start()
        else:
            print(">Uang Tidak Cukup<")
            paymentsewa()
    elif pilihan == "2":
        print("================Nota Pembayaran===============")
        print("Pc no: " , pc)
        print("Harga yang di bayar: Rp. ", harga)
        print("ID Transaksi: GPT-",order)
        print("No Referensi: ", ref)
        print("Metode Pembayaran : VIA GOPAY")
        print("==============================================")
        start()
    elif pilihan == "3":
        sewa()
    else:
        print("Silahkan Pilih Metode Pembayaran Yang Ada !")
        paymentsewa()

def paymentinap():
    print("======Silahkan Pilih Metode Pembayaran========")
    print("1. Cash")
    print("2. Gopay")
    print("==============================================")
    print("3. Kembali")
    print("==============================================")
    pilihan = input("Pilih Metode Pembayaran : ")
    if pilihan == "1":
        uang = int(input("Uang Yang Diterima : "))
        if uang >= paketx:
            balik = uang - paketx
            print("================Nota Pembayaran===============")
            print("Paket pilihan no: " , pilihan)
            print("Harga yang perlu di bayar: Rp. ", paketx)
            print("Uang Diterima : ", uang)
            print("Kembalian : ", balik)
            print("Metode Pembayaran : Cash")
            print("==============================================")
            start()
        else:
            print(">Uang Tidak Cukup<")
            paymentsewa()
    elif pilihan == "2":
        print("================Nota Pembayaran===============")
        print("Paket pilihan no: " , pilihan)
        print("Harga yang di bayar: Rp. ", paketx)
        print("ID Transaksi: GPT-",order)
        print("No Referensi: ", ref)
        print("Metode Pembayaran : VIA GOPAY")
        print("==============================================")
        start()
    elif pilihan == "3":
        menginap()
    else:
        print("Silahkan Pilih Metode Pembayaran Yang Ada !")
        paymentinap()

start()