print("Welkom bij de Nano App Store!")
print("1. Nummer Raad Spel")
import Nano
import SprintIII  # van journal management
import SprintI  # Dit module bevat het nummer raden spel
import rps  # Dit module bevat Rock, Paper, Scissors spel

while True:
    print("Welkom bij de Nano App Store!")  # Print het keuze menu
    print("Kies een van de volgende opties:")
    print("1. Nummer Raad Spel")  # Start het nummer raden spel
    print("2. Rock, Paper, Scissors")  # Start het Rock, Paper, Scissors spel
    print("3. Dagboek beheren")
    print("4. Exit")

    choice = input("Maak je keuze (1, 2, 3 of 4): ")
    if choice == '1':
        SprintI.nummer_raad_spel()
    elif choice == '2':
        NanoM.my_rps_game()  #Hier vastgelopen en
    elif choice == '3':
        SprintIII.manage_journal()
    elif choice == '4':
        print("Bedankt voor het gebruik maken van Nano. Tot ziens!")
        break
    else:
        print("Ongeldige keuze, probeer opnieuw.")

