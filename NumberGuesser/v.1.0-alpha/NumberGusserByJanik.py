from operator import truediv

###
print("This game is alpha and some functions doesnt work")
###

def print_lang_menu():
    print("1. Slovak")
    print("2. English")

print_lang_menu()
option = int(input("Select your language: "))

while option != 0:
    if option == 1:
        def slovak_menu():
            print("1. Guess 1 - 10")
            print("2. Guess 1 - 100")
            print("3. Guess 1 - 1000")
        
        slovak_menu()
        option = int(input("Select game: "))

        while option!= 0:
            if option == 1:
                import random

                n = random.randint(1,10)
                print("Mylsim nad cislom medzi 1 az 10")

                running = True
                while running:
                    guess_str = input("Hádaj: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VYHRAL SI!!!")
                        running = False
                    elif guess < n:
                        print("Väčšie")
                    else:
                        print("Mänšie")
            elif option == 2:
                import random

                n = random.randint(1,100)
                print("Myslim nad cislom medzi 1 az 100")

                running = True
                while running:
                    guess_str = input("Hádaj: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VYHRAL SI!!!")
                        running = False
                    elif guess < n:
                        print("Väčšie")
                    else:
                        print("Mänšie")
            elif option == 3:
                import random

                n = random.randint(1,1000)
                print("Myslim nad cislom medzi 1 az 1 000")

                running = True
                while running:
                    guess_str = input("Hádaj: ")
                    guess = int(guess_str)
                    if guess == n:
                        print("VYHRAL SI!!!")

                    elif guess < n:
                        print("Väčšie")
                    else:
                        print("Mänšie")

            
                        
                        

    elif option == 2:
        print("English")
        def english_menu():
            print("1. Guess 1 - 10")
            print("2. Guess 1 - 100")
            print("3. Guess 1 - 1000")
        
        english_menu()
        option = int(input("Select level: "))

        while option!= 0:
            while option == 1:
                import random
                
                n = random.randint(1,10)

                #
                print("Im thinking abou number between 1 - 10")

                running = True

    
    elif option == 3:
        print("NumberGuesserByJanik")
        print("")
        print("alpha.1.0")
        print("This game is alpha and some functions doesnt work")





    else:
        print("What the hell")

    print()
    print_lang_menu()
    option = int(input("Select your language: "))

print("Tank ya")