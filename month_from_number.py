#!/usr/bin/env python 3
#
# Created by: Dahrio Francois
# Created on: December 2020
# this program takes a number from 1 - 12
#     & displays the month


def main():
    # this function prints a month from a number from 1 - 12

    # input
    month = int(input("Enter your number value: "))
    print("")

    # process & output
    if month == 1:
        print(" January ")

    elif month == 2:
        print(" February ")

    elif month == 3:
        print(" March ")

    elif month == 4:
        print(" April ")

    elif month == 5:
        print(" May ")

    elif month == 6:
        print(" June ")

    elif month == 7:
        print(" July ")

    elif month == 8:
        print(" August ")

    elif month == 9:
        print(" September ")

    elif month == 10:
        print(" October ")

    elif month == 11:
        print(" November ")

    elif month == 12:
        print(" December ")


if __name__ == "__main__":
    main()
