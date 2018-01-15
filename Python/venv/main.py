import random
import sys
import os


def get_y_n(message):
    while True:
        return_value = input(message+" y/n").lower()
        if return_value == "y" or return_value == "n":
            break
        else:
            print("Wrong input! Please enter y or n: ")
    return return_value


def get_password_info():
    while True:
        try:
            length = int(input("How long your password should be? "))
            break
        except ValueError:
            print("Not an integer!")
    capital = get_y_n("Should it contain uppercase letters too?")
    numbers = get_y_n("Should it contain numbers?")
    special = get_y_n("Should it contain special characters?")

    return_value = (length, capital, numbers, special)
    return return_value


def main():
    used_characters="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num="0123456789"
    spec="_-*@:!,+-=()[]{}#&"
    password=""

    while True:
        password_info = get_password_info()
        if password_info[1] == "y":
            used_characters+=uppercase
        if password_info[2] == "y":
            used_characters += num
        if password_info[3] == "y":
            used_characters += spec
        length_of_characters = len(used_characters)
        for x in range(1, password_info[0] + 1):
            password += used_characters[random.randint(0,
                                        length_of_characters - 1)]
        print(password)
        ex = input("Would you like to generate another password? y/n")
        if ex == "n":
            break
        password = "";
        used_characters = "abcdefghijklmnopqrstuvwxyz"


main()