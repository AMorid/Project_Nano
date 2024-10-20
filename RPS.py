# Opdracht: Nano
# Naam: Morid Aziz
# Studentnummer: 1861078
import random  # Importeer de volledige random module

def get_computer_choice():
    # Kies willekeurig uit de lijst
    choices = ["Rock", "Paper", "Scissors"]  # Mogelijke keuzes
    return random.choice(choices)  # Gebruik random.choice() om een willekeurige keuze te maken

def de_winner(user_choice, computer_choice):
    # Functie om de winnaar te bepalen
    if user_choice == computer_choice:
        return "It's a tie! What a pity!"  #Gelijkspel
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Paper" and computer_choice == "Rock") or \
            (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win! ""keep going..!"  # I win
    else:
        return "You lose:( But don't worry, you'll get them next time!"

def my_rps_game():
    # de functie voor Rock, Paper, Scissors spel
    print("Welcome to my Rock, Paper, Scissors - the easy edition!")
    while True: # while-loops
        user_choice = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").capitalize()

        if user_choice == 'Exit':
            print("Thanks for playing RPS! See you next time!")
            break  # Exit en Spel stoppen

        if user_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")  # Ongeldige keuze
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = de_winner(user_choice, computer_choice)
        print(result)

my_rps_game()
