print("Tip Calculator")
tagihan = float(input("Berapa total tagihannya? Rp"))
persen_tip = float(input("Berapa persen tip yang ingin Anda berikan? [5] [10] or [15] ? "))
jumlah_orang = float(input("Ada berapa banyak orang untuk membagi tagihan? "))

tagihan_tip = persen_tip / 100 * tagihan

total_tagihan = tagihan + tagihan_tip

per_orang = total_tagihan / jumlah_orang

print(f"Setiap orang harus membayar: Rp{per_orang:.2f}")