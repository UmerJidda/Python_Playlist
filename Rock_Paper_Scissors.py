import random
input("Press Enter to start the game")
Rock = 1
Paper = 2
Scissors = 3
user_input = input("Select Rock, Paper or Scissors\n")
list= ["Rock", "Paper", "Scissors"]
computer_input = random.choice(list)
print(f"Computer selected {computer_input}")
print("user selected", user_input)
user_score = 0
computer_score = 0
while (user_score < 5 and computer_score < 5):
    if user_input == computer_input:
        print("It's a tie")
    elif user_input == "Rock" and computer_input == "Scissors":
        print("User wins")
        user_score += 1
    elif user_input == "Paper" and computer_input == "Rock":
        print("User wins")
        user_score += 1
    elif user_input == "Scissors" and computer_input == "Paper":
        print("User wins")
        user_score += 1
    else:
        print("Computer wins")
        computer_score += 1
    print(f"User score: {user_score} Computer score: {computer_score}")
    if user_score == 5:
        print("User wins the game")
    elif computer_score == 5:
        print("Computer wins the game")
    else:
        user_input = input("Select Rock, Paper or Scissors\n")
        computer_input = random.choice(list)
        print(f"Computer selected {computer_input}")
        print("user selected", user_input)