import random

# Word categories
word_bank = {
    "fruits": ["apple", "banana", "orange", "mango", "grape", "melon"],
    "animals": ["tiger", "elephant", "giraffe", "lion", "zebra", "monkey"],
    "countries": ["india", "canada", "brazil", "germany", "japan", "france"],
     "cars": ["audi", "bmw", "mercedes", "honda", "toyota", "tesla"],
     "colors": ["red", "blue", "green", "black", "white", "pink"],
    "sports": ["cricket", "tennis", "chess", "football", "hockey", "golf"],
    "vehicles": ["car", "bus", "train", "truck", "bike", "scooter"],
    "clothes": ["shirt", "jeans", "socks", "cap", "jacket", "skirt"],
    "school": ["pen", "book", "bag", "chair", "desk", "chalk"]
}

# Ask for player name
player_name = input("Enter your name: ").strip().capitalize()
print(f"\n Welcome, {player_name}! Let's play the word guessing game!")

# Score tracking
wins = 0
losses = 0

#  Main Game Function 
def play_game():
    global wins, losses

    print("\nChoose a category:")
    categories = list(word_bank.keys())
    for i in range(len(categories)):
        print(f"{i+1}. {categories[i]}")

    choice = input("Enter number: ")

    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected_category = categories[int(choice) - 1]
    else:
        print("Invalid choice. Defaulting to 'fruits'.")
        selected_category = "fruits"

    word = random.choice(word_bank[selected_category])
    guessed = ["_"] * len(word)
    tries = 6
    guessed_letters = []

    while tries > 0 and "_" in guessed:
        print(f"\nPlayer: {player_name}")
        print("Category:", selected_category.capitalize())
        print("Word:", " ".join(guessed))
        print("Guessed letters:", " ".join(guessed_letters))
        print("Tries left:", tries)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print(" Correct!")
        else:
            tries -= 1
            print(" Wrong!")

    # Result
    if "_" not in guessed:
        print(f"\n Well done, {player_name}! You guessed the word: {word}")
        wins += 1
    else:
        print(f"\n Sorry, {player_name}. Game over! The word was: {word}")
        losses += 1

    print(f"\n {player_name}'s Score: {wins} Win(s), {losses} Loss(es)")

# Leaderboard Functions 

def save_score(name, wins, losses):
    scores = {}

    # Read existing scores
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                line = line.strip()
                if ": " in line:
                    player, record = line.split(": ")
                    win_part, loss_part = record.split(", ")
                    w = int(win_part.split(" ")[0])
                    l = int(loss_part.split(" ")[0])
                    scores[player] = (w, l)
    except FileNotFoundError:
        pass

    # Update score
    if name in scores:
        prev_wins, prev_losses = scores[name]
        scores[name] = (prev_wins + wins, prev_losses + losses)
    else:
        scores[name] = (wins, losses)

    # Write updated scores
    with open("leaderboard.txt", "w") as file:
        for player, (w, l) in scores.items():
            file.write(f"{player}: {w} wins, {l} losses\n")

def show_leaderboard():
    print("\n Leaderboard:")
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No scores yet.")

# Game Loop with Replay 

while True:
    play_game()
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print(f"\n Thanks for playing, {player_name}!")
        print(f" Final Score: {wins} Wins, {losses} Losses")
        
        save_score(player_name, wins, losses)
        show_leaderboard()
        break
         