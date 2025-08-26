import random as r
guess = r.randint(1,100)
print(guess)

def number_guessing_game():
        while True:
            player_guess = int(input("Enter your guess : "))
            if guess == player_guess:
                print("Congratulations! You guessed right number.")
                break
            elif guess < player_guess:
                print("Too High!")
                pass
            else:
                print("Too Low")
                pass

def car_game():
    started = False
    print("""
start -To start the car
stop  -To stop the car
exit  -To exit the game
help  -To get user guide""")
    while True:
        player_command = input("Enter your choice: ")
        if player_command == "help":
            print("""
start -To start the car
stop  -To stop the car
exit  -To exit the game
help  -To get user guide
""")    
        elif player_command == "start":
            if not started:
                started = True
                print("Car started...")
            elif started:
                print("Car is already started!")

        elif player_command == "stop":
            if started:
                started = False
                print("Car Stopped...")
            elif not started:
                print("Car is already stopped!")

        else:
            break




car_game()