print("=========================================")
print("     PROGRAM MENGHITUNG JARAK TITIK      ")
print("=========================================\n")

# Input jumlah titik (n > 1)
n = 0
while n <= 1:
    a = input("Masukkan jumlah titik : ")
    angka = True
    if len(a) == 0:
        angka = False
    else:
        for i in a:
            if i < '0' or i > '9':
                angka = False
                break
    if angka:
        n = int(a)
        if n <= 1:
            print("Jumlah titik harus lebih dari 1.\n")
    else:
        print("Input harus angka bulat!\n")

# Input koordinat titik-titik
print("\nMasukkan koordinat titik dalam format x,y (boleh negatif dan desimal)")
titik = []
i = 0
while i < n:
    a = input(f"Titik ke-{i+1}: ")

    # Cari posisi koma
    koma_index = -1
    for j in range(len(a)):
        if a[j] == ',':
            koma_index = j
            break

    if koma_index == -1:
        print("Format salah! Gunakan koma (x,y)\n")
        continue

    x = ""
    y = ""
    j = 0
    while j < koma_index:
        x += a[j]
        j += 1
    j = koma_index + 1
    while j < len(a):
        y += a[j]
        j += 1

    # Validasi x_text
    x_valid = True
    titik_x = 0
    pos_minus = -1
    if len(x) == 0:
        x_valid = False
    else:
        for index_c in range(len(x)):
            c = x[index_c]
            if c == '-':
                pos_minus = index_c
            if c == '.':
                titik_x += 1
            elif c == '-' and index_c != 0:
                x_valid = False
            elif c < '0' or c > '9':
                if c != '-' and c != '.':
                    x_valid = False
        if titik_x > 1:
            x_valid = False
        if pos_minus > 0:
            x_valid = False

    # Validasi y
    y_valid = True
    titik_y = 0
    pos_minus = -1
    if len(y) == 0:
        y_valid = False
    else:
        for index_c in range(len(y)):
            c = y[index_c]
            if c == '-':
                pos_minus = index_c
            if c == '.':
                titik_y += 1
            elif c == '-' and index_c != 0:
                y_valid = False
            elif c < '0' or c > '9':
                if c != '-' and c != '.':
                    y_valid = False
        if titik_y > 1:
            y_valid = False
        if pos_minus > 0:
            y_valid = False

    if x_valid and y_valid:
        x = float(x)
        y = float(y)
        titik.append([x, y])
        i += 1
    else:
        print("Koordinat harus berupa angka valid (boleh negatif dan desimal)\n")

# Tampilkan titik-titik yang dimasukkan
print("\nTitik-titik yang dimasukkan:")
index = 0
while index < n:
    print(f"  titik{index+1} = ({titik[index][0]}, {titik[index][1]})")
    index += 1

# Hitung dan tampilkan jarak antar titik
print("\nJarak antar titik:")
i = 0
while i < n:
    j = i + 1
    while j < n:
        dx = titik[i][0] - titik[j][0]
        dy = titik[i][1] - titik[j][1]
        jarak = (dx*dx + dy*dy) ** 0.5
        print(f"  Jarak titik{i+1} ke tutik{j+1} = {jarak:.3f}")
        j += 1
    i += 1

print("======================================")
print("               SELESAI                ")
print("======================================")