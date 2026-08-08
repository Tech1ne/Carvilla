import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "tie"
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "player" if beats[player] == computer else "computer"

def play():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    print("Rock, Paper, Scissors! Type 'quit' to stop.\n")

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if player_choice == "quit":
            break
        if player_choice not in choices:
            print("Invalid choice, try again.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = get_winner(player_choice, computer_choice)

        if result == "tie":
            print("It's a tie!\n")
        elif result == "player":
            player_score += 1
            print("You win this round!\n")
        else:
            computer_score += 1
            print("Computer wins this round!\n")

        print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

    print(f"\nFinal Score -> You: {player_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play()
