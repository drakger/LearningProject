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


main()
'''
divisors = []
found=0
while True:
    try:
        dividend = int(input("Give me a number: \n"))
        if dividend<0:
            dividend*=-1
    except ValueError:
        print("Not an integer! Try again")
        dividend=None
    if dividend==0:
        print("Every integer is a divisor of 0")
    elif dividend==1:
        print("1 is only divisible by itself")
    elif dividend is None:
        print("")
    else:
        for x in range(1, dividend//2+1):
            if dividend%x==0:
                for y in divisors:
                    if y.find(str(x))>-1:
                        found=1
                if found==0:
                    divisors.append("("+str(x)+","+str(int(dividend/x))+")")
                else:
                    found=0
        for x in divisors:
            print(x)
        divisors=[]
'''

'''
list_a_size = random.randint(1, 20)
list_b_size = random.randint(1,20)
a=[]
b=[]
for x in range(1, list_a_size):
    a.append(random.randint(1,100))
for x in range(1, list_b_size):
    b.append(random.randint(1,100))

intersect=list(set(a).intersection(set(b)))
print("First list:",a)
print("Second list:",b)
if intersect:
    print("Intersections are: ",intersect)
else:
    print("The lists do not intersect")
'''




