#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: May 25th, 2025
# This program takes the level from the user and returns the percentage mark
def calc_mark(level):

    match level:
        case "4+":
            return 100
        case "4":
            return 90
        case "4-":
            return 85
        case "3++":
            return 80
        case "3+":
            return 77
        case "3":
            return 73
        case "3-":
            return 70
        case "2++":
            return 67
        case "2+":
            return 63
        case "2":
            return 60
        case "2-":
            return 57
        case "1++":
            return 53
        case "1+":
            return 50
        case "1":
            return 45
        case "1-":
            return 40
        case _:
            return "Invalid Level"


def main():
    # Gets the level of the user.
    user_level = input("Enter your level (e.g., 4+, 3, 2-): ")
    # Checks the percentage mark of the user's level.
    mark = calc_mark(user_level)
    # Displays the mark of the user
    print(f"The calculated mark is: {mark}")


if __name__ == "__main__":
    main()
