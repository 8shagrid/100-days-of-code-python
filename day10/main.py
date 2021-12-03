import os
from art import logo

def tambah(n1, n2):
  return n1 + n2

def kurang(n1, n2):
  return n1 - n2

def kali(n1, n2):
  return n1 * n2

def bagi(n1, n2):
  return n1 / n2

operasi = {
  "+": tambah,
  "-": kurang,
  "*": kali,
  "/": bagi
}

def calculator():
  print(logo)

  num1 = float(input("Masukkan angka:\n> "))
  
  lanjut = True
  while lanjut:
    simbol_operasi = input("Pilih Operasi: ")
    num2 = float(input("Masukkan angka:\n> "))
    fungsi_perhitungan = operasi[simbol_operasi]
    jawaban = fungsi_perhitungan(num1, num2)
    print(f"{num1} {simbol_operasi} {num2} = {jawaban}")

    pilih = input(f"Ketik 'LANJUT' untuk melanjutkan penghitungan dengan {jawaban}, atau ketik 'BARU' untuk memulai penghitungan baru: ").lower()
    if pilih == 'lanjut':
      num1 = jawaban
    elif pilih == 'baru':
      lanjut = False
      os.system('cls')
      calculator()
    else:
      lanjut = False


calculator()
