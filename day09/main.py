import os
from art import logo

tawaran = {}

def cari_bid_tertinggi(catatan_penawaran):
    tawaran_tertinggi = 0
    pemenang = ""
    for penawar in catatan_penawaran:
        jumlah_tawaran = catatan_penawaran[penawar]
    if jumlah_tawaran > tawaran_tertinggi:
        pemenang = penawar
        tawaran_tertinggi = jumlah_tawaran
    print(f"Pemenangnya adalah {pemenang} dengan tawaran sebesar Rp{tawaran_tertinggi}")

penawaran_selesai = False
while not penawaran_selesai:
    print(logo)
    nama = input("Nama Penawar: ")
    harga = int(input("Tawaran Harga: Rp"))
    tawaran[nama] = harga 
    jawaban = input("Tambahkan tawaran baru? 'ya' atau 'tidak': ").lower()
    if jawaban == 'tidak':
        penawaran_selesai = True
        cari_bid_tertinggi(tawaran)
    elif jawaban == 'ya':
        os.system('cls')