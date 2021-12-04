from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Memeriksa tebakan user
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Terlalu Tinggi.")
    return turns - 1
  elif guess < answer:
    print("Terlalu Rendah.")
    return turns - 1
  else:
    print(f"Kamu Benar! Jawabannya adalah {answer}.")

#Fungsi untuk memilih tingkat kesulitan.
def set_difficulty():
  level = input("Pilih kesulitan. Ketik 'mudah' atau 'sulit': ").lower()
  if level == "mudah":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Memilih nomor acak antara 1 dan 100.
  print("Welcome to the Number Guessing Game!")
  print("Tebak angka antara 1 - 100.")
  answer = randint(1, 100)
   

  turns = set_difficulty()
  #Ulangi fungsi menebak jika salah.
  guess = 0
  while guess != answer:
    print(f"\nKamu memiliki {turns} tebakan tersisa.")

    #input user untuk menebak angka.
    guess = int(input("Ayo Tebak!\n> "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("\nTebakan sudah habis, Anda kalah.")
      print(f"Jawaban yang benar adalah {answer}")
      return
    elif guess != answer:
      print("Tebak Ulang.")

game()

