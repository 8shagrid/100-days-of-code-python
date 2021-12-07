from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc} from {account_country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

print(logo)
score = 0
game_should_continue = True
b = random.choice(data)

while game_should_continue:

  a = b
  b = random.choice(data)
  while a == b:
    b = random.choice(data)

  print(f"Compare A: {format_data(a)}")
  print(vs)
  print(f"Compare B: {format_data(b)}")

  guess = input("Who has more followers? type 'A' or 'B': ").lower()

  a_follower_count = a["follower_count"]
  b_follower_count = b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  os.system('cls')
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}.")

  

