print ( "===== Sistem Panduan Keselamatan Bencana Alam ===== ")

# database bencana alam
bencana_alam = [
        ( "Gempa bumi",
          "Gempa bumi adalah getaran atau guncangan pada permukaan bumi yang disebabkan oleh pelepasan energi secara tiba-tiba di dalam bumi.",
        [
            "Lindungi kepala dan badan Anda dari reruntuhan bangunan (dengan bersembunyi di bawah meja, dll",
            "Berlari keluar apabila masih dapat dilakukan.",
            "Mencari tempat yang paling aman dari reruntuhan goncangan",
            "Jauhi bangunan, pohon besar, dan tiang listrik."
        ]),

        ( "Tsunami",
          "Tsunami adalah gelombang air besar yang diakibatkan oleh gangguan di dasar laut, seperti gempa bumi, longsor bawah laut, dan letusan gunung berapi.",
        [
            "Segera evakuasi ke tempat tinggi atau tempat aman lain",
            "Segera jauhi pantai setelah terjadi goncangan",
            "Hindari jembatan atau bangunan yang rapuh.",
            "Dengarkan informasi resmi dari BMKG"
        ]),

        ( "Letusan vulkanik",
          "Letusan gunung berapi merupakan peristiwa yang terjadi akibat magma di dalam perut bumi yang keluar oleh gas yang bertekanan tinggi. Peristiwa ini berhubungan dengan naiknya magma putih dari dalam perut bumi.",
          [
              "Gunakan pakaian tertutup untuk melindungi kulit",
              "Gunakan masker dan kacamata pelindung.",
              "Hindari daerah aliran sungai, karena bisa dilalui lahar.",
              "Ikuti jalur evakuasi resmi."
          ]),

        ( "Badai topan",
          "Badai topan adalah angin puting beliung berskala besar dengan kecepatan tinggi, biasanya di atas 120 km/jam, yang terjadi di wilayah tropis di antara garis balik utara dan selatan.",
        [
            "Tetap di dalam rumah atau bangunan yang kokoh, jauh dari jendela.",
            "Matikan listrik jika ada genangan air untuk menghindari korslet.",
            "Jika rumah tidak aman, segera pindah ke tempat evakuasi yang disediakan",
            "Jangan keluar rumah sebelum pihak berwenang menyatakan aman."
        ]),       
]

# tampilkan daftar
print ("Daftar bencana: ")
print ("1.", bencana_alam [0][0] )
print ("2.", bencana_alam [1][0] )
print ("3.", bencana_alam [2][0] )
print ("4.", bencana_alam [3][0] )

#pilih bencana yg ingin dicari tahu
pilih = input("Masukkan nomor bencana yang ingin dipilih (1-4)")

if pilih in ["1", "2", "3", "4"]:
    tanya = input( "Apakah ingin tau panduan keselamatannya? (ya/tidak)")
    if tanya.lower() == "ya":
        indeks = int (pilih) -1
        print("Deskripsi:", bencana_alam[indeks][1])
        print("Panduan keselamatan:")
        print("1.", bencana_alam[indeks][2][0])
        print("2.", bencana_alam[indeks][2][1])
        print("3.", bencana_alam[indeks][2][2])
        print("4.", bencana_alam[indeks][2][3])
else:
    print ("Nomor yang Anda masukkan tidak valid.")


#CRUD
print("\n===== MENU CRUD =====")
print("1. Tambah bencana")
print("2. Ubah bencana")
print("3. Hapus bencana")
print("4. Tampilkan daftar")

pilihan = input("Masukkan pilihan (1-4): ")

#create

if pilihan == "1":
    nama = input("Masukkan nama bencana: ")
    deskripsi = input("Masukkan deskripsi: ")
    tips1 = input("Cara 1: ")
    tips2 = input("Cara 2: ")
    tips3 = input("Cara 3: ")
    tips4 = input("Cara 4: ")
    bencana_alam.append((nama, deskripsi, [tips1, tips2, tips3, tips4]))
    print(f"{nama} berhasil ditambahkan.")
    print("\nDaftar bencana terbaru:")
    if len(bencana_alam) > 0: print("1.", bencana_alam[0][0])
    if len(bencana_alam) > 1: print("2.", bencana_alam[1][0])
    if len(bencana_alam) > 2: print("3.", bencana_alam[2][0])
    if len(bencana_alam) > 3: print("4.", bencana_alam[3][0])
    if len(bencana_alam) > 4: print("5.", bencana_alam[4][0])

#update

elif pilihan == "2":
    nomor = int(input("Masukkan nomor bencana yang ingin diubah: ")) - 1
    if 0 <= nomor < len(bencana_alam):
        nama = input("Nama baru: ")
        deskripsi = input("Deskripsi baru: ")
        bencana_alam[nomor] = (nama, deskripsi, bencana_alam[nomor][2])
        print("Data berhasil diubah.")
        print("\nDaftar bencana terbaru:")
        if len(bencana_alam) > 0: print("1.", bencana_alam[0][0])
        if len(bencana_alam) > 1: print("2.", bencana_alam[1][0])
        if len(bencana_alam) > 2: print("3.", bencana_alam[2][0])
        if len(bencana_alam) > 3: print("4.", bencana_alam[3][0])
        if len(bencana_alam) > 4: print("5.", bencana_alam[4][0])
    else:
      print("Nomor tidak valid.")

#delete

elif pilihan == "3":
    Nomor = int(input("Masukkan nomor bencana yang ingin dihapus: ")) - 1
    if 0 <= Nomor < len(bencana_alam):
        nama = bencana_alam[Nomor][0]
        bencana_alam.pop(Nomor)
        print(f"{nama} berhasil dihapus.")

        print("\nDaftar bencana terbaru:")
        if len(bencana_alam) > 0: print("1.", bencana_alam[0][0])
        if len(bencana_alam) > 1: print("2.", bencana_alam[1][0])
        if len(bencana_alam) > 2: print("3.", bencana_alam[2][0])
        if len(bencana_alam) > 3: print("4.", bencana_alam[3][0])
        if len(bencana_alam) > 4: print("5.", bencana_alam[4][0])
    else:
      print("Nomor tidak valid.")

# READ / tampilkan daftar
elif pilihan == "4":
    print("\nDaftar bencana :")
    if len(bencana_alam) > 0: print("1.", bencana_alam[0][0])
    if len(bencana_alam) > 1: print("2.", bencana_alam[1][0])
    if len(bencana_alam) > 2: print("3.", bencana_alam[2][0])
    if len(bencana_alam) > 3: print("4.", bencana_alam[3][0])

else:
    print("Menu tersebut tidak valid")
