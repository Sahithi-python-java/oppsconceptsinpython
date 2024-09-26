import random  # Importing the random module to generate random numbers

def generate_secret_number():
    """Generates a 4-digit random number with unique digits."""
    # random.sample() is used to generate a list of 4 unique digits from 0 to 9
    digits = random.sample(range(10), 4)
    # Convert the list of digits into a string
    return ''.join(map(str, digits))

def get_cows_and_bulls(secret_number, guess):
    """Calculates the number of cows and bulls for a given guess."""
    # Bulls: Correct digit in the correct position
    bulls = sum(1 for i in range(4) if guess[i] == secret_number[i])
    # Cows: Correct digit, but in the wrong position
    cows = sum(1 for i in range(4) if guess[i] in secret_number and guess[i] != secret_number[i])
    return cows, bulls

def cows_and_bulls_game():
    # Introduction to the game
    print("Welcome to the Cows and Bulls Game!")
    print("You need to guess a 4-digit number with unique digits.")
    print("For each guess, you'll get feedback on cows and bulls.")
    print("Bulls: Correct digit and correct position.")
    print("Cows: Correct digit but wrong position.")
    print("You have 10 chances to guess the number.\n")
    
    # Generate the secret number for the player to guess
    secret_number = generate_secret_number()
    attempts = 10  # Number of attempts (chances) the player has to guess

    # The loop will run until the player runs out of attempts (10 attempts)
    while attempts > 0:
        # Prompt the user to input their 4-digit guess
        guess = input(f"Attempt {11 - attempts}/10 - Enter your 4-digit guess: ")
        
        # Validation to check if the input is exactly 4 digits and has unique digits
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Please enter a valid 4-digit number with unique digits.")
            continue  # Skip to the next iteration if the input is invalid

        # Calculate the number of cows and bulls for the guess
        cows, bulls = get_cows_and_bulls(secret_number, guess)
        
        # Provide feedback to the player on how many cows and bulls they got
        print(f"Cows: {cows}, Bulls: {bulls}")
        
        # If the player gets 4 bulls, they guessed the number correctly and win
        if bulls == 4:
            print(f"Congratulations! You guessed the number {secret_number} correctly.")
            break  # Exit the loop since the game is won
        
        # Decrement the number of attempts left
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.\n")  # Inform the player of remaining attempts
        else:
            # If the player runs out of attempts, reveal the secret number and end the game
            print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Entry point for the game to start when the script is run
if __name__ == "__main__":
    cows_and_bulls_game()  # Start the game
