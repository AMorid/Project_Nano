# Opdracht: Beroepsproduct project Nano App Store
# Naam: Morid Aziz
# Studentnummer: 111000010110010111110
# Bronen: Presentaties uit de les. W3school, Python.org, een regeltje chatGPT, namelijk: regel 150.
# https://github.com/AMorid/Nanom.git
# Als test push ik deze weer!
import random
import datetime
import os
import json
# Sprint 1: nummer raden
def nummer_raad_spel():
    print("Welcome to the Guessing Game!\nTry to guess the number between 1 and 25.")
    print("LET OP! You have only 5 attempts")
    number = random.randrange(1, 25)
    guess = int(input("Enter your guess: "))
    attempt = 5
    while attempt > 1 and number != guess:
        attempt -= 1  # Verminder het aantal poging
        if guess < number:  # if-statement
            print(f"Too low! You have {attempt} attempts left.")
            guess = int(input("Guess again: "))  # Vraag opnieuw om een gok
        elif guess > number:
            print(f"Too high! You have {attempt} attempts left.")
            guess = int(input("Guess again: "))
        else:
            break    # Verlaat de loop als het getal juist is
    if guess == number:
        print("Hoera! You guessed t right!:)")
    else:
        print(f"Oepsi, you've run out of attempts! The correct number was {number}.")
# Sprint 2, Dagboekje
# De e datum van de gebruiker te krijgen
def get_date_from_user():
    choice = input("Wilt u een dagboek voor vandaag schrijven of een andere datum? (vandaag/anders): ").lower()
    if choice == 'vandaag':
        return datetime.date.today()
    else:
        date_str = input("Voer de datum in (YYYY-MM-DD): ")
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Ongeldige datum, probeer opnieuw.")
            return get_date_from_user()
def get_file_path(date):
    return f"files/{date}.json"
def check_file_exists(file_path):   # of het bestand bestaat
    return os.path.exists(file_path)   # True or false
def ask_questions():
    questions = [
        "Hoe was je dag?",
        "Waar ben je dankbaar voor?",
        "Wat heb je vandaag bereikt?",
        "Heb je obstakels of uitdagingen gehad?",
        "Wat heb je geleerd en wat wil je verbeteren?"
    ]
    answers = {}
    for question in questions:
        answer = input(question + "\n")
        # Vraag om input voor elke vraag \n voor de regel volgorde
        answers[question] = answer
    return answers
def write_to_file(file_path, data, append=False):
    if append:
        # de antwoorden naar een bestand te schrijven r= read w= write
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
        existing_data.update(data)
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4) # Schrijf bijgewerkte data naar het bestand
    else:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)   # Schrijf de nieuwe data naar een nieuw bestand
def manage_journal():
    todaydate = get_date_from_user()
    file_path = get_file_path(todaydate)
    if check_file_exists(file_path):
        choice = input(
            f"Er bestaat al een dagboek voor {todaydate}. Wilt u tekst toevoegen of herschrijven? (toevoegen/herschrijven): ").lower()
        if choice == 'toevoegen':
            new_data = ask_questions()   # Vraag voor de nieuwe gegevens
            write_to_file(file_path, new_data, append=True)
            # Voeg de gegevens toe aan het bestaande bestand
        elif choice == 'herschrijven':
            new_data = ask_questions()
            write_to_file(file_path, new_data, append=False)
            # Overschrijf het bestaande besta
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
    else:
        print(f"Geen dagboek gevonden voor {todaydate}. Een nieuwe dagboek wordt aangemaakt.")
        new_data = ask_questions()
        write_to_file(file_path, new_data)
# Sprint 1: Rock, Paper, Scissors een simpel en extra spel.
def get_computer_choice():
    # Kies willekeurig uit de lijst
        choices = ["Rock", "Paper", "Scissors"]  # Mogelijke keuzes
        return random.choice(choices)
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
# Sprint 3 voor mijn hoofdmenu
def main_menu():
    while True:
        print("\nWelkom bij de Nano App Store!")
        print("1. Raad Spel")  # Start het nummer raden spel
        print("2. Rock, Paper, Scissors")   # Start het Rock, Paper, Scissors spel
        print("3. Dagboek")
        print("4. Exit")
        choice = input("Maak je keuze (1, 2, 3 of 4): ")
        # if, elif, eles statements sgebruikt
        if choice == '1':
            nummer_raad_spel()
        elif choice == '2':
            my_rps_game()
        elif choice == '3':
            manage_journal()
        elif choice == '4':
            print("Bedankt voor het gebruik maken van Nano. Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
# Start mijn platform
if __name__ == "__main__":
    # Hier heel klein beetje chat gebruikt.
    os.makedirs("files", exist_ok=True)
    # Start mijn hoofdmenu
    main_menu()

# (To-DO lijs voor de NANO XL)
# Voeg een wachtwoord toe aan het dagboek
# Geef de gebruiker de mogelijkheid om de tekst van een dag op te vragen en te lezen
# Geef de gebruiker de mogelijkheid om een tekst te bewerken
