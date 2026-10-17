# game.py

from game_world import GameWorld

def main():
    game_world = GameWorld()
    game_world.setup_characters()
    game_world.setup_locations()
    game_world.setup_clues()

    print("Welcome to 'Murder at Summit Lodge'!")
    print("You are an internal investigator tasked with solving the murder of Jonathan Reed.")
    print("You have access to various locations, characters, and clues to help you solve the case.")

    # Provide initial information
    print("\nInitial Information:")
    print("- Time of Death: Approximately between 8:10 PM and 8:20 PM.")
    print("- Cause of Death: Single gunshot wound.")
    print("- Victim: Jonathan Reed, CEO of Summit Technologies.")
    print("- Location Found: CEO's Office at Summit Lodge.")
    print("- Weather Conditions: Severe storm causing power fluctuations.")
    print("- All guests are company executives attending a retreat.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Investigate a location")
        print("2. Talk to a character")
        print("3. Review collected clues")
        print("4. Accuse a suspect")
        print("5. Exit game")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            game_world.investigate_location()
        elif choice == '2':
            game_world.talk_to_character()
        elif choice == '3':
            game_world.review_clues()
        elif choice == '4':
            game_world.accuse_suspect()
        elif choice == '5':
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Add line separator between turns
        print("----------------------------------------------------")

if __name__ == "__main__":
    main()