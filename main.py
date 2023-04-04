import random

print("Lets play rock, paper, scissors!\n")

options = ["rock", "paper", "scissors"]

roundsWon = 0

for i in range(3):
  print(f"Round {i+1}\n")
  while (True):
    user_option = input("Choose your option: ")

    if (user_option in options):
      print("Valid option")
      computer_option = random.choice(options)
      print(f"The computer chose {computer_option}")

      if (user_option == computer_option):
        print("Draw :|\n")
      elif ((user_option == "rock" and computer_option == "scissors")
            or (user_option == "paper" and computer_option == "rock")
            or (user_option == "scissors" and computer_option == "paper")):
        print(f"You won round {i+1}! :D\n")
        roundsWon += 1
      else:
        print(f"You lose round {i+1}! D:\n")
      break
    else:
      print("Invalid option\n")

if (roundsWon >= 2):
  print(f"You won {roundsWon} of 3 rounds. You are the winner")
else:
  print("Loser")

print("Game finished")
