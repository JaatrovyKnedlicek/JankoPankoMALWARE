#import
from operator import truediv
import os
import sys
import subprocess


#lang menu
def print_lang_menu():
    print("1. Slovak")
    print("2. English")
    print("3. About")

print_lang_menu()
option = int(input("Select your language: "))
#SK
while option != 0:
    if option == 1:
        def slovak_menu():
            os.system("cls")
            print("1. Guess 1 - 10")
            print("2. Guess 1 - 100")
            print("3. Guess 1 - 1000")
        
        slovak_menu()
        option = int(input("Select game: "))

        while option!= 0:
            if option == 1:
                import random
                os.system("cls")
                n = random.randint(1,10)
                print("Mylsim nad cislom medzi 1 az 10")
                

                running = True
                while running:
                    guess_str = input("Hádaj: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VYHRAL SI!!!")
                        running = False
                        input("Stlač akú kolvek klávesu pre ukončenie hry")
                        sys.exit()

                    elif guess < n:
                        print("Väčšie")
                    else:
                        print("Mänšie")
            elif option == 2:
                import random
                os.system("cls")
                n = random.randint(1,100)
                print("Myslim nad cislom medzi 1 az 100")

                running = True
                while running:
                    guess_str = input("Hádaj: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VYHRAL SI!!!")
                        running = False
                        input("Stlač akú kolvek klávesu pre ukončenie hry")
                        sys.exit()

                    elif guess < n:
                        print("Väčšie")
                    else:
                        print("Mänšie")
            elif option == 3:
                import random

                n = random.randint(1,1000)
                print("Myslim nad cislom medzi 1 az 1 000")
                os.system("cls")
                running = True
                while running:
                    guess_str = input("Hádaj: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VYHRAL SI!!!")
                        running = False
                        input("Stlač akú kolvek klávesu pre ukončenie hry")
                        sys.exit()

                    elif guess < n:
                        print("Väčšie")
                    else:
                        print("Mänšie")

            
                        
                        
#english
    elif option == 2:
        print("English")
        def english_menu():
            os.system("cls")
            print("1. Guess 1 - 10")
            print("2. Guess 1 - 100")
            print("3. Guess 1 - 1000")
        
        english_menu()
        option = int(input("Select level: "))

        while option!= 0:
            while option == 1:
                import random
                os.system("cls")
                n = random.randint(1,10)

                #
                print("Im thinking abou number between 1 - 10")

                running = True
                while running:
                    guess_str = input("Take a guess: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VICTORY!!!")
                        running = False
                        input("Press any key to close the game")
                        sys.exit()
                    elif guess < n:
                        print("Bigger")
                    else:
                        print("Smaller")

            while option == 2:
                import random
                os.system("cls")
                n = random.randint(1,100)

                
                print("Im thinking abou number between 1 - 100")

                running = True
                while running:
                    guess_str = input("Take a guess: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VICTORY!!!")
                        running = False
                        input("Press any key to close the game")
                        sys.exit()
                    elif guess < n:
                        print("Bigger")
                    else:
                        print("Smaller")
                
            while option == 3:
                import random
                os.system("cls")
                n = random.randint(1,1000)
                
                print("Im thinking abou number between 1 - 1000")

                running = True
                while running:
                    guess_str = input("Take a guess: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VICTORY!!!")
                        running = False
                        input("Press any key to close the game")
                        sys.exit()

                    elif guess < n:
                        print("Bigger")
                    else:
                        print("Smaller")
                    
#about    
    elif option == 3:
        print("NumberGuesserByJanik")
        print("")
        print("1.2")
        print("Maked on Pyrhon 3.10.7 64-bit")
        print("Thank you for playing")
        print("Complete specification in about.txt file")
        print("")
        input("Press any key to close...")
        os.system("cls")





    else:
        print("Incorent option")

    print()
    print_lang_menu()
    option = int(input("Select your language: "))

print("Tank ya")