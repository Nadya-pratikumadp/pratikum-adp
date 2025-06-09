file_baru = "data_keuangan.txt"

def file_ada ():
    f = open(file_baru, "a")
    f.close ()
    f = open(file_baru, "r")
    ada = False
    if f.read() != "":
        ada = True
    f.close()
    return ada

def load_data ():
    data = []
    f = open(file_baru, "r")
    baris = f.readlines()
    for line in baris:
        line = line.strip()
        if line:
            bagian = line.split('|')
            if len(bagian) == 4:
                tanggal, keterangan, jumlah, tipe = bagian
                data.append({
                    'Tanggal': tanggal,
                    'Keterangan': keterangan,
                    'Jumlah': jumlah,
                    'Tipe': tipe
                })
    f.close()
    return data

def simpan_data (data):
    f = open(file_baru, "w")
    for item in data:
        line = item['Tanggal'] + '|' + item['Keterangan'] + '|' + item['Jumlah'] + '|' + item['Tipe'] + '\n'
        f.write(line)
    f.close()

def tampilkan_data (data):
    if len(data) == 0:
        print("\nTidak ada data yang tersimpan")
    else:
        print("\n=======DATA KEUANGAN=======")
        for i in range (len(data)):
            item = data[i]
            print(str(i+1) + ". Tanggal : " + item['Tanggal'])
            print(" Keterangan : " + item['Keterangan'])
            print(" Jumlah : " + item['Jumlah'])
            print(" Tipe : " + item['Tipe'])

def tambah_data(data):
    tanggal = input("Masukkan tanggal (yyyy-mm-dd) : ")
    keterangan = input("Masukkan keterangan         : ")
    jumlah = input("Masukkan jumlah uang        : ")
    tipe = input("Masukkan tipe (pengeluaran/pemasukan) : ").lower()

    if tipe == 'pengeluaran' or tipe == 'pemasukan':
        item = {
            'Tanggal': tanggal,
            'Keterangan': keterangan,
            'Jumlah': jumlah,
            'Tipe': tipe
        }
        data.append(item)
        simpan_data(data)
        print("Data berhasil disimpan!")
    else:
        print("Tipe tidak valid. Data tidak disimpan.")

def hapus_data(data):
    tampilkan_data(data)
    if len(data) == 0:
        return

    index = input("Masukkan nomor data yang ingin dihapus : ")
    if index.isdigit():
        index = int(index) - 1
        if index >= 0 and index < len(data):
            keterangan = data[index]['Keterangan']
            for i in range(index, len(data)-1):
                data[i] = data[i+1]
            data.pop()  # hapus elemen terakhir (duplikat)
            simpan_data(data)
            print("Data dengan keterangan '" + keterangan + "' berhasil dihapus!")
        else:
            print("Nomor data tidak valid.")
    else:
        print("Input tidak valid.")

def main():
    # Pastikan file ada
    file_ada()

    data = load_data()

    while True:
        print("\n=== Menu Keuangan ===")
        print("1. Tambah data keuangan")
        print("2. Hapus data keuangan")
        print("3. Tampilkan semua data")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            tambah_data(data)
        elif pilihan == '2':
            hapus_data(data)
        elif pilihan == '3':
            tampilkan_data(data)
        elif pilihan == '4':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")

if __name__ == "__main__":
    main()

