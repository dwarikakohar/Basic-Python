import random as r
guess = r.randint(1,100)
print(guess)
total_attempts = 0
def number_guessing_game():
    global total_attempts
    while True:
        player_guess = int(input("Enter your guess : "))
        total_attempts += 1
        if guess == player_guess:
            print(f"Congratulations! You guessed it right in {total_attempts} attempts")
            break
        elif guess < player_guess:
            print("Too High!")
            pass
        else:
            print("Too Low")
            pass
            
number_guessing_game()