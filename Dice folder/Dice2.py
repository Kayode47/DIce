import random

dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

def roll():
    return random.randint(1, 6)

def play_game():
    while True:
        print("-" * 50)
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("-" * 50)
                print("Invalid number of players. Enter the number of players (2-4):")
        else:
            print("-" * 50)
            print("Invalid input, please try again")

    print("-" * 50)
    print(f"Great! You have {players} players!")

    max_score = 50
    player_scores = [0 for _ in range(players)]  # Reset scores for each game

    while max(player_scores) < max_score:
        for player_idx in range(players):
            print("\nPlayer number", player_idx + 1, "turn has just started!")
            print("Your total score is:", player_scores[player_idx], "\n") 
            current_score = 0

            while True:
                print("-" * 50)
                should_roll = input("Would you like to roll? (y) ")
                if should_roll.lower() != "y":
                    break

                value = roll()
                if value == 1:
                    print("-" * 50)
                    print(f"You rolled: {dice_faces[value]} ({value})")
                    current_score = 0
                    print("-" * 50)
                    print("Oh no! You rolled a 1, your turn has ended.")
                    break
                else:
                    current_score += value
                    print("-" * 50)
                    print(f"You rolled: {dice_faces[value]} ({value})")

                if player_scores[player_idx] + current_score > max_score:
                    print("-" * 50)
                    print("You exceeded the max score! Your turn ends.")
                    current_score = max_score - player_scores[player_idx]
                    break

                print("-" * 50)
                print("Your score is:", current_score)

            player_scores[player_idx] += current_score
            print("-" * 50)
            print("Your total score is:", player_scores[player_idx])

    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print("-" * 50)
    print("Player Number", winning_idx + 1,
        "is the winner with a score of:", max_score)

    # Ask if they want to play again
    play_again = input("\nWould you like to play again? (y/n) ").lower()
    if play_again == "y":
        play_game()  # Restart the game
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
play_game()
