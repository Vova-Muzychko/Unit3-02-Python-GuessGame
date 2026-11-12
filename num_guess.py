#!/usr/bin/env python3
# Created by: Vova
# Created on: November 12, 2026
# This program asks the user to guess a number between 0 and 9
# and checks if it matches the correct constant number.

import constants


def main():
    # Ask the user to guess a number
    guessed_number = int(input("Enter a number between 0 and 9: "))

    # Check if the guess is correct
    if guessed_number == constants.CORRECT_NUMBER:
        print("You guessed correctly!")

    # Check if the guess is incorrect
    if guessed_number != constants.CORRECT_NUMBER:
        print(f"You guessed wrong. The correct number is {constants.CORRECT_NUMBER}.")


if __name__ == "__main__":
    main()
