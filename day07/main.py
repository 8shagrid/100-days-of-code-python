import random
import os
from hangman_art import logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Membuat List Kosong
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f"Nyawa: {lives}")
    guess = input("Tebak huruf: ").lower()

    os.system('cls')

    if guess in display:
      print(f"Huruf '{guess}' sudah ditebak.")

    #Memeriksa huruf yang ditebak
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Memeriksa jika pengguna salah.
    if guess not in chosen_word:
        print(f"Kamu menebak '{guess}', tidak ada dalam kata. Kamu kehilangan Nyawa.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Kamu Kalah.")
            print(f'Jawabannya adalah {chosen_word}.')
        

    #List diubah menjadi sebuah String.
    print(f"{' '.join(display)}")

    #Memeriksa jika user telah berhasil menebak semua surat.
    if "_" not in display:
        end_of_game = True
        print("Kamu Menang.")

    from hangman_art import stages
    print(stages[lives])