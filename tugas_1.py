print("==================== Resto GEN Z ======================")
print("===================== SELAMAT DATANG===================")
print("\n")
print("==================== MENU RESTO =======================")
print("------------------------------------------------------")
print("|PAKET|           ISI               |  HARGA  |")
print("------------------------------------------------------")
print("|  1  |   NASI SOTO+ ES TEH         |Rp. 20.000|")
print("|  2  | NASI AYAM RICA RICA+ES TEH  |Rp. 40.000|")
print("|  3  | NASI AYAM SAUS KEJU+ES TEH  |Rp. 42.000|")
print("|  4  |   NASI AYAM BAKAR+ ES TEH   |Rp. 36.000|")
print("|  5  |   AYAM RICA RICA+ ES TEH    |Rp. 35.000|")
print("|  6  |   AYAM SAUS KEJU+ ES TEH    |Rp. 37.000|")
print("------------------------------------------------------")
print("\n")
print("\n")
print("--- Masukkan Identitas Pemesanan ---")
nama=input  ("Nama Lengkap                    :")
no=input    ("No HP                           :")
alamat=input("Alamat Lengkap                  :")
x=(input    ("paket yang di inginkan          :"))
y=int(input ("jumlah paket yang ingin di pesan:"))
a=20000
b=40000
c=42000
d=36000
e=35000
f=37000
if x=="1": 
    t=("Nasi Soto + Es Teh")
    harga=y*a
elif x=="2":
    t=("NASI AYAM RICA RICA+ES TEH")
    harga=y*b
elif x=="3":
    t=("NASI AYAM SAUS KEJU+ES TEH")
    harga=y*c
elif x=="4":
    t=("NASI AYAM BAKAR+ ES TEH")
    harga=y*d
elif x=="5":
    t=("AYAM RICA RICA+ ES TEH")
    harga=y*e
else:
    t=("AYAM SAUS KEJU+ ES TEH")
    harga=y*f
pajak=int(harga*(10/100))
if harga<150000:
    biaya_pengiriman=25000
else:
    biaya_pengiriman=0
total=harga+pajak+biaya_pengiriman
print("\n")
print("=======================================================")
print("                   STRUK PEMESANAN                     ")
print("=======================================================")
print("Nama:", nama)
print("No HP:", no)
print("Alamat Pengiriman:", alamat)
print("Detail Pemasanan : Paket",x,"{",b,"}")
print("Jumlah Pemesanan :",y)
print("Total Harga      :Rp", harga)
print("Pajak (10%)      :Rp", pajak)
print("Biaya Pengiriman :", biaya_pengiriman)
print("Total Akhir      :", total)
print("=================SELAMAT MENIKMATI=====================")
print("=======================================================")