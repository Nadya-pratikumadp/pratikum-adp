def input_data():
    pratikan = []
    while True:
        nama = input("Masukkan nama pratikan (atau ketik 'selesai' untuk mengakhiri): ")
        if nama == 'selesai':
            print("Input dihentikan.")
            break
        nim = input("Masukkan NIM pratikan: ")
        nilai_pretest = float(input("Masukkan nilai pretest: "))
        nilai_postest = float(input("Masukkan nilai postest: "))
        nilai_tugas = float(input("Masukkan nilai tugas makalah: "))
        nilai_bonus = float(input("Masukkan nilai bonus: "))

        nilai_akhir = (0.25 * nilai_pretest) + (0.25 * nilai_postest) + (0.50 * nilai_tugas) + nilai_bonus

        pratikan.append({
            'nama': nama,
            'nim': nim,
            'nilai_akhir': nilai_akhir
        })
    return pratikan

def hitung_rata_rata(pratikan):
    total = 0
    for p in pratikan:
        total += p['nilai_akhir']
    if len(pratikan) > 0:
        return total / len(pratikan)
    else:
        return 0

#jumlah = int(input("Masukkan jumlah praktikan: "))

def tampilkan_tabel(pratikan, rata_rata):
    print("\n{:<20} {:<10} {:<15} {:<10}".format("Nama", "NIM", "Nilai Akhir", "Peringkat"))
    print("=" * 60)
    index = 0
    while index < len(pratikan):
        p = pratikan[index]
        print(p['nama':20], "\t\t", p['nim'], "\t\t", f"{p['nilai_akhir']:.2f}", "\t\t", index + 1)
        print(f"{nama:<20} | {nim:<10} | {nilai_akhir:<15.2f}","{:<10}",index+1)
        index += 1
    print("Rata-rata Nilai Akhir:", f"{rata_rata_nilai_akhir:.2f}")

# Program utama

pratikan = input_data()

# Sorting dengan bubble sort descending berdasarkan nilai_akhir
n = len(pratikan)
for i in range(n):
    for j in range(0, n - i - 1):
        if pratikan[j]['nilai_akhir'] < pratikan[j + 1]['nilai_akhir']:
            pratikan[j], pratikan[j + 1] = pratikan[j + 1], pratikan[j]

rata_rata_nilai_akhir = hitung_rata_rata(pratikan)
tampilkan_tabel(pratikan, rata_rata_nilai_akhir)




