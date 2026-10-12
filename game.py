import random as r

choices = ["rock", "paper", "scissors"]

wins = 0
losses = 0
ties = 0

while True:
    player = input("Rock, Paper or Scissors? (type quit to stop): ").lower()
    if player == "quit":
        break
    if player not in choices:
        print("Invalid choice.")
        continue
    computer = r.choice( choices )
    
    print("You chose:", player)
    print("You chose:", computer)
    
    if player == computer:
        print("Its a tie!!!")
        ties += 1
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        print("You win!!!(this time;))")
        wins += 1
    else:
        print("You lose!!!(unexpectedly")
        losses += 1
    
print("\n Final Score")
print("Wins", wins)
print("Ties", ties)
print("Losses", losses)
print

        
