import random
def guess_number():
    number_to_guess=random.randint(1,100)
    print(number_to_guess)
    wrong_guess=True
    attempts = 1
    while wrong_guess:
        guess = int(input('Guess the number (between 1 and 100): '))
        if guess > number_to_guess: print("Too high! Try again.")
        elif guess < number_to_guess: print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            wrong_guess=False
        print()
        attempts += 1
        if attempts >10:
            print("Game over! Better luck next time!")
            break
guess_number()


