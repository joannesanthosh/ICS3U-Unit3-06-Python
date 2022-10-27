#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program gets the user to guess a number correctly or incorrectly

import random


def main():
    # this function checks if the guess is correct

    # input
    random_number = random.randint(0, 9)  # a number between 0 and 9
    user_guess_as_string = input("Enter a number between 0-9: ")
    print("")

    # process & output
    try:
        user_guess_as_number = int(user_guess_as_string)
        if user_guess_as_number == random_number:
            print("Correct guess!")
        else:
            print("Incorrect. The number was: {0}.".format(random_number))
    except ValueError:
        print("This was not an integer")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
