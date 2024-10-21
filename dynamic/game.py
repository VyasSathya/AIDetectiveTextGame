# game.py

import openai
from character import Character
from location import Location
from clue import Clue
from game_world import GameWorld
import os

api_key = os.getenv('OPENAI_API_KEY')

def main():
    # Initialize the game world
    game_world = GameWorld()
    game_world.setup_characters()
    game_world.setup_locations()
    game_world.setup_clues()
    
    print("Welcome to 'Murder at Summit Lodge'!")
    print("You are an internal investigator tasked with solving the murder of Jonathan Reed.")
    
    # Main game loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Investigate a location")
        print("2. Talk to a character")
        print("3. Review clues")
        print("4. Accuse a suspect")
        print("5. Exit game")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            game_world.investigate_location()
        elif choice == '2':
            game_world.talk_to_character()
        elif choice == '3':
            game_world.review_clues()
        elif choice == '4':
            game_world.accuse_suspect()
            # Do not exit the game after accusation; allow continued play
        elif choice == '5':
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()