#import
from operator import truediv
import os
import sys
import subprocess


#lang menu
def print_lang_menu():
    print("1. Slovak")
    print("2. English")

print_lang_menu()
option = int(input("Select your language: "))
#SK
while option != 0:
    if option == 1:
        def slovak_menu():
            os.system("cls")
            print("1. Hádaj 1 - 10")
            print("2. Hádaj 1 - 100")
            print("3. Hádaj 1 - 1000")
            print("4. Hádaj 1 - 10000")
            print("9. Informácie")

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

            while option == 4:
                import random
                os.system("cls")
                n = random.randint(1,10000)

                
                print("Rozmýšlam nad číslom medzi 1 - 10 000")

                running = True
                while running:
                    guess_str = input("Hádaj: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("Vyhral si!!!")
                        running = False
                        input("Niečo stlač a ono sa to vypne...")
                        sys.exit()
                    elif guess < n:
                        print("Väčšie")
                    else:
                        print("Mänšie")
            
            
            while option == 9:
                def aboutSK():
                    os.system("cls")
                    print("NumberGuesserByJanik")
                    print("")
                    print("1.2")
                    print("Maked on Python 3.10.7 64-bit")
                    print("Thank you for playing")
                    print("Complete specification in about.txt file")
                    print("")
                    input("Press any key to close...")
                    sys.exit()
                        

                aboutSK()
                        
#english
    elif option == 2:
        print("English")
        def english_menu():
            os.system("cls")
            print("1. Guess 1 - 10")
            print("2. Guess 1 - 100")
            print("3. Guess 1 - 1000")
            print("4. Guess 1 - 10000")
            print("9. About")
        
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


            while option == 4:
                import random
                os.system("cls")
                n = random.randint(1,10000)

                
                print("Im thinking abou number between 1 - 10 000")

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

            while option == 9:
                def aboutEN():
                            os.system("cls")
                            print("NumberGuesserByJanik")
                            print("")
                            print("1.2")
                            print("Maked on Python 3.10.7 64-bit")
                            print("Thank you for playing")
                            print("Complete specification in about.txt file")
                            print("")
                            input("Press any key to close...")
                            sys.exit()

                aboutEN()




    else:
        print("Incorent option")

    print()
    print_lang_menu()
    option = int(input("Select your language: "))

print("Tank ya")