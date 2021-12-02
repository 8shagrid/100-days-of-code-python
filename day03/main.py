print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Selamat datang di Pulau Harta Karun.")
print("Misi Kamu adalah menemukan harta karun.")

print('''Kamu berada di persimpangan jalan. Ke mana kamu mau pergi? Ketik "kiri" atau "kanan"''')
pilihan1 = input("> ").lower()
if pilihan1 == 'kiri':
  print('''Kamu datang ke sebuah danau. Ada sebuah pulau di tengah danau. Ketik "tunggu" untuk menunggu kapal. Ketik "berenang" untuk berenang menyeberang''')
  pilihan2 = input("> ").lower()
  if pilihan2 == 'tunggu':
    print('''Kamu tiba di sebuah pulau tanpa cedera. Ada sebuah rumah dengan 3 pintu. Satu "merah", satu "kuning", dan satu "biru". Warna apa yang kamu pilih?''')
    pilihan3 = input("> ").lower()
    if pilihan3 == 'merah':
      print("Terbakar oleh api. Game Over.")
    elif pilihan3 == 'kuning':
      print("Kamu Menang!")
    elif pilihan3 == 'biru':
      print("Dimakan oleh binatang buas. Game Over.")
    else:
      print("Game Over")
  else:
    print("Diserang oleh monster ikan. Game Over.")
else:
  print("Jatuh ke dalam lubang. Game Over.")
