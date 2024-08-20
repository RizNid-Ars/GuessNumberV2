import random


def start_game():
    attempts = 3
    capital = 100
    while attempts != 0:
        guess_number = int(input("Enter a number to guess from 1 to 5: "))
        random_number = random.randint(1, 6)
        if guess_number == random_number:
            print(f"You guessed the number in {attempts} attempts.")
            capital *= 2
        else:
            print(f'You guessed wrong number in {attempts} attempts. Number is {random_number}.')
            capital -= 50
        if capital == 0:
            print("You lose.")
            break
        attempts -= 1
        print(f"Your capital is {capital}.")
