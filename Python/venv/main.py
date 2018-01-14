import random
import sys
import os
def main():
    used_characters="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num="0123456789"
    spec="_-*@:!,+-=()[]{}#&"
    password=""
    while True:
        while True:
            try:
                length=int(input("How long your password should be? "))
                while True:
                    capital=input("Should it contain uppercase letters too? y/n").lower()
                    if capital=="y" or capital=="n":
                        while True:
                            numbers = input("Should it contain numbers? y/n").lower()
                            if numbers== "y" or numbers == "n":
                                while True:
                                    special= input("Should it contain special characters? y/n").lower()
                                    if special == "y" or special == "n":
                                        break
                                    else:
                                        print("Wrong input!")
                                break
                            else:
                                print("Wrong input!")
                        break
                    else:
                        print("Wrong input!")
                break
            except ValueError:
                print("Not an integer!")
        if capital=="y":
            used_characters+=uppercase
        if numbers=="y":
            used_characters+=num
        if special=="y":
            used_characters+=spec
        length_of_characters=len(used_characters)
        for x in range(1, length+1):
            password+=used_characters[random.randint(0,length_of_characters-1)]
        print(password)
        ex=input("Would you like to generate another password? y/n")
        if ex=="n":
            break
        password="";
        used_characters = "abcdefghijklmnopqrstuvwxyz"

print("Testing")
main()