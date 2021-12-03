alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, jumlah_pergeseran, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    jumlah_pergeseran *= -1
  
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + jumlah_pergeseran
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"\nHere's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

berhenti = False
while not berhenti :
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n> ")
  text = input("\nType your message:\n> ").lower()
  shift = int(input("\nType the shift number:\n> "))
  shift = shift % 26

  caesar(text=text, jumlah_pergeseran=shift, cipher_direction=direction)

  result = input("\nType 'yes' if you want to go again, Otherwise type 'no'.\n> ").lower()
  if result == 'no':
    berhenti = True