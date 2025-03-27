print("RESERVASI TIKET KONSER NCT:", "\n")

n=15
m=8
total_kursi=n*m
harga_tiket_vvpi   = 15000000
harga_tiket_vpi    = 10000000
harga_tiket_reguler= 5000000
harga_tiket_ekonomi= 2500000

print("\n")
print("MENAMPILKAN TATA LETAK KURSI KONSER NCT")
for a in range (1,61):
    print(" ", a, end="      ")
    if a%15==0:
        print()
        a +=1
for a in range (61,121):
    print(" ", a, end="      ")
    if a%15==0:
        print()
        a +=1

print("\n")
print("========HARGA TIKET:========")
print("VVIP      Rp 15000000")
print("VIP       Rp 10000000")
print("REGULER   Rp 5000000 ")
print("EKONOMI   Rp 2500000 ")
print("=============================","\n")

jumlah_pemesanan=int(input("masukkan jumlah tiket yang ingin dipesan   :"))

terpesan_vvip    = 0
terpesan_vip     = 0
terpesan_reguler = 0
terpesan_ekonomi = 0
for a in range (1, jumlah_pemesanan+1):
    print                 (f"pemesanan ke -                             :{a}")
    nama=input            ("masukkan nama pemesanan                    :")
    no_kursi=int(input    ("masukkan no kursi yang di inginkan         :"))
    password=input        ("buat password konser                       :")
    if 1<=no_kursi<=30:
        kategori = "VVIP"
        harga_tiket= 15000000
        terpesan_vvip += 1
    elif 30<no_kursi<=60:
        kategori = "VIP"
        harga_tiket= 10000000
        terpesan_vip += 1
    elif 60<no_kursi<=90:
        kategori = "reguler"
        harga_tiket= 5000000
        terpesan_reguler += 1
    elif 90<no_kursi<121:
        kategori="Ekonomi"
        harga_tiket= 2500000
        terpesan_ekonomi += 1
    else:
        kategori=("-")
        harga_tiket=("-")
    print("\n")
    print("======STRUK PEMESANAN TIKET KONSER=======")
    print("Nama:",nama)
    print("Nomor Kursi",no_kursi)
    print("Kategori",kategori)
    print("Harga",harga_tiket)
    print("Password Konser",password)
    print("============TERIMA KASIH==================","\n")

sisa_kursi_vvip=30-terpesan_vvip
print("Sisa Kursi VVIP",sisa_kursi_vvip)
sisa_kursi_vip=30-terpesan_vip
print("Sisa Kursi VIP",sisa_kursi_vip)
sisa_kursi_reguler=30-terpesan_reguler
print("Sisa Kursi REGULER",sisa_kursi_reguler)
sisa_kursi_ekonomi=30-terpesan_ekonomi
print("Sisa Kursi EKONOMI",sisa_kursi_ekonomi)

print("\n")
for b in range (1,61):
    print(" ", b, end="      ")
    if b%15==0:
        print()
        b +=1
        a=b-b
        if b== no_kursi:
            b==0
            print(b)
            
for b in range (61,121):
    print(" ", b, end="      ")
    if b%15==0:
        print()
        b +=1
        a=b-b
        if b== no_kursi:
            b==0
            print(b)

print("TERIMA kASIH TELAH MELAKUKAN RESERVASI")
