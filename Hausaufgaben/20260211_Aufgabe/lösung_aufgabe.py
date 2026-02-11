import random

# #Aufgabe 1

# zahl = int(input("Geben Sie ein Zahl ein: "))

# for i in range(1, 11):
#     result = i * zahl
#     print(f"{i} * {zahl} = {result}")

#Aufgabe 2 

# quess_number = random.randint(1,10)
# #print(quess_number) -- hack string
# while True:
#     players_number = int(input("Geben Sie Ihre Zahl ein: "))
#     if players_number == quess_number:
#         print("You Win") 
#         break
#     else:
#         print("You lose. Try again!")

# #Aufgabe 3

# quess_number = random.randint(1,10)
# #print(quess_number) -- hack string
# while True:
#     players_number = int(input("Geben Sie Ihre Zahl ein: "))
#     if players_number > quess_number:
#         print("The number is greater than quess number")
#     elif players_number < quess_number:
#         print("The number is less than quess number")
#     else:
#         print("You Win.")


def main():
    start_game()

def quess_number():
    return random.randint(1,10)
    #print(quess_number) -- hack string

def show_menu():
    print("1. Start Game")
    print("2. Exit")
    choose = input("What r u want? Start (1) or Exit (2)")
    match choose:
        case "1":
            start_game()
        case "2":
            return exit_from_game()    

def start_game():
    quess = quess_number()
    while True:
        players_number = int(input("Geben Sie Ihre Zahl ein: "))
        if players_number > quess:
            print("The number is greater than quess number")
        elif players_number < quess:
            print("The number is less than quess number")
        else:
            print("You Win. Wanna u play again?")
            answer = input("Yes or No? ")
            if answer == "Yes":
                start_game()
            elif answer == "No":
                return exit_from_game()
            
def exit_from_game():
    return "Exit"

main()