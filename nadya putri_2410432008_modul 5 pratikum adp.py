# Inisialisasi list untuk menyimpan data
nomor_mahasiswa = []
nama_mahasiswa = []
nilai_mahasiswa = []


# Program utama
while True:
    print("=== Menu Manajemen Nilai Mahasiswa ===")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        # Tambah Data
        nama  = input ("Masukkan Nama  Mahasiswa: ")
        nomor = int(input ("Masukkan Nomor Mahasiswa: "))
        nilai = float(input ("Masukkan nilai Mahasiswa: "))
        nomor_mahasiswa.append(nomor)
        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)
        print("Data berhasil ditambahkan.\n")

    elif pilihan == '2':
        # Hapus Data
        nomor = input("Masukkan Nomor Mahasiswa yang ingin dihapus: ")
        if nomor in nomor_mahasiswa:
            index = nomor_mahasiswa.index(nomor)
            del nomor_mahasiswa[index]
            del nama_mahasiswa[index]
            del nilai_mahasiswa[ index]
            # del nomor_mahasiswa (index)
            # del nama_mahasiswa (index)
            # del nilai_mahasiswa (index)
            print("Data berhasil dihapus.\n")
        else:
            print("Nomor mahasiswa tidak ditemukan.\n")

    elif pilihan == '3':
        # Tampilkan Data
        if len(nomor_mahasiswa) == 0:
            print("Belum ada data mahasiswa.\n")
        else:
            # Gabungkan data ke dalam satu list 
            data_keseluruhan = []
            for i in range(len(nomor_mahasiswa)):
                data_keseluruhan.append((nomor_mahasiswa[i], nama_mahasiswa[i], nilai_mahasiswa[i]))

            # Urutkan berdasarkan nilai 
            a = len (data_keseluruhan)
            batas = a
            while batas > 1 :
                for i in range (batas-1):
                    if data_keseluruhan[i][2] < data_keseluruhan [i+1][2]:
                        data_mahasiswa = data_keseluruhan [i]
                        data_keseluruhan[i] = data_keseluruhan [i+1]
                        data_keseluruhan [i+1] = data_mahasiswa
                batas -=1

            # Tampilkan data
            print("\nData Mahasiswa telah di urutkan berdasarkan nilai:")
            print("------------------------------------------")
            print("No.      | Nama                    | Nilai")
            print("------------------------------------------")
            for data in data_keseluruhan:

                print(f"{data[0]:<5} | {data[1]:<20} | {data[2]}")
            print()


    elif pilihan == '4':
        # Keluar dari program
        print("Terima Kasih. Program Telah Selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")

