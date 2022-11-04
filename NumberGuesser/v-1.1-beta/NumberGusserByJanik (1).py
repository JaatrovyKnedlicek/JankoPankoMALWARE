from operator import truediv
import os

###
print("BETA VERSION!!!")
###

def print_lang_menu():
    print("1. Slovak")
    print("2. English")
    print("3. About")

print_lang_menu()
option = int(input("Select your language: "))

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
                        os.system("cls")
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
                        os.system("cls")
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
                        os.system("cls")
                    elif guess < n:
                        print("Väčšie")
                    else:
                        print("Mänšie")

            
                        
                        

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
                        os.system("cls")
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
                        os.system("cls")
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
                        os.system("cls")
                    elif guess < n:
                        print("Bigger")
                    else:
                        print("Smaller")
                    
    
    elif option == 3:
        print("NumberGuesserByJanik")
        print("")
        print("beta-1.1")
        print("You are playing beta version and some thinks dont work.")
        print("")
        input("Press any key to close...")
        os.system("cls")





    else:
        print("What the hell")

    print()
    print_lang_menu()
    option = int(input("Select your language: "))

print("Tank ya")