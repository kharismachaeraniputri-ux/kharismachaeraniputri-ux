#263307107_vending_v0_4.py
# Vending Machine v

def tampilkan_menu():
    print("=" * 45)
    print("         SELAMAT DATANG DI VENDING MACHINE")
    print("=" * 45)
    print("1. Keripik Singkong  Rp5,000   Stok: 4")
    print("2. Susu Coklat       Rp7,000   Stok: 6")
    print("3. Roti Bakar        Rp10,000  Stok: 3")
    print("=" * 45)

def hitung_total(harga, jumlah):
    return harga * jumlah

# Menampilkan menu utama
tampilkan_menu()

# Input pilihan produk dan jumlah
pilihan = int(input("Pilih nomor produk (1-3): "))
jumlah = int(input("Jumlah beli: "))

# Inisialisasi variabel produk
nama_produk = ""
harga_produk = 0
stok_produk = 0

if pilihan == 1:
    nama_produk = "Keripik Singkong"
    harga_produk = 5000
    stok_produk = 4
elif pilihan == 2:
    nama_produk = "Susu Coklat"
    harga_produk = 7000
    stok_produk = 6
elif pilihan == 3:
    nama_produk = "Roti Bakar"
    harga_produk = 10000
    stok_produk = 3
else:
    nama_produk = "Tidak valid"

# Validasi pilihan produk yang tersedia
if nama_produk != "Tidak valid":
    # Validasi stok (if luar)
    if stok_produk >= jumlah:
        total = hitung_total(harga_produk, jumlah)
        print(f"Total harga untuk {jumlah} {nama_produk}: Rp{total:,}")
        
        uang = int(input("Uang dibayar: "))
        cukup = uang >= total
        
        # Validasi saldo / uang dengan nested if (if dalam)
        if cukup:
            kembalian = uang - total
            print(f"Berhasil! Kembalian: Rp{kembalian:,}")
        else:
            kekurangan = total - uang
            print(f"Uang tidak cukup. Kurang Rp{kekurangan:,}")
    else:
        print(f"Maaf, stok {nama_produk} tidak cukup (sisa stok: {stok_produk})")
else:
    print("Maaf, pilihan produk tidak valid.")