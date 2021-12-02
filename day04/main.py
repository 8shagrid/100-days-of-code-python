import random

batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

kertas = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

gambar = [batu, gunting, kertas]

user_pilih = int(input("Ketik [0] untuk Batu, [1] untuk Gunting atau [2] untuk Kertas.\nKamu memilih:\n> "))
print(gambar[user_pilih])

computer_pilih = random.randint(0, 2)
print("Komputer memilih:")
print(f"> {computer_pilih}")
print(gambar[computer_pilih])

if user_pilih >= 3 or user_pilih < 0: 
  print("> Nomor tidak valid, Anda kalah!") 
elif user_pilih == 0 and computer_pilih == 2:
  print("> Kamu Kalah!")
elif computer_pilih == 0 and user_pilih == 2:
  print("> Kamu Menang!")
elif computer_pilih > user_pilih:
  print("> Kamu Menang!")
elif user_pilih > computer_pilih:
  print("> Kamu Kalah!")
elif computer_pilih == user_pilih:
  print("> Seimbang!")
