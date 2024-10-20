# main.py

from game_world import World
from storyteller import Storyteller
from agent import Agent
from world_time import WorldTime
from dialogue import Dialogue

MAX_TURNS = 10

# main.py

# main.py

def interrogate(world, storyteller):
    print("\nWho would you like to interrogate?")
    for idx, agent in enumerate(world.agents):
        print(f"{idx + 1}. {agent.name}")
    
    choice = int(input("\nChoose a suspect by number: ")) - 1
    if 0 <= choice < len(world.agents):
        chosen_agent = world.agents[choice]
        dialogue = Dialogue(chosen_agent, "Player", world)  # Pass world here
        clue = dialogue.initiate()
        if clue:  # Only add the clue if it's not None
            storyteller.add_clue_to_notebook(clue)
    else:
        print("Invalid choice.")

def review_notebook(storyteller):
    print("\n--- Notebook Review ---")
    storyteller.display_notebook()

def solve_crime(storyteller, world):
    storyteller.reveal_final_suspect(world)

def cross_off_suspect(storyteller, world):
    print("\nWho would you like to cross off the suspect list?")
    for idx, suspect in enumerate(world.suspects):
        if suspect not in storyteller.suspects_crossed_off:
            print(f"{idx + 1}. {suspect}")

    choice = int(input("\nChoose a suspect by number to cross off: ")) - 1
    if 0 <= choice < len(world.suspects):
        suspect = world.suspects[choice]
        if suspect not in storyteller.suspects_crossed_off:
            storyteller.cross_off_suspect(suspect)
        else:
            print(f"{suspect} has already been crossed off.")
    else:
        print("Invalid choice.")

def player_actions(world, storyteller):
    turns_left = MAX_TURNS
    while turns_left > 0:
        print(f"\nYou have {turns_left} turns left.")
        print("What would you like to do?")
        print("1. Interrogate a suspect")
        print("2. Review notebook")
        print("3. Cross off a suspect")
        print("4. Solve the crime")
        print("5. Quit")

        choice = input("\nChoose an action: ")

        if choice == "1":
            interrogate(world, storyteller)
            turns_left -= 1
        elif choice == "2":
            review_notebook(storyteller)
        elif choice == "3":
            cross_off_suspect(storyteller, world)  # Cross off suspects actively
        elif choice == "4":
            storyteller.reveal_final_suspect(world)
            break
        elif choice == "5":
            print("Goodbye, Detective!")
            break
        else:
            print("Invalid choice. Try again.")

    if turns_left == 0:
        print("\nYou’ve run out of turns! You must solve the crime now.")
        storyteller.reveal_final_suspect(world)

def run_game():
    storyteller = Storyteller()
    world_time = WorldTime()
    world = World(storyteller, ["House", "Office", "Park"], world_time)

    # Add agents (suspects and witnesses)
    alice = Agent("Alice", "Suspect", "Money", "Was at work", "Mislead")
    bob = Agent("Bob", "Suspect", "No motive", "Saw Alice", "Help")  # Mark Bob as a suspect
    carol = Agent("Carol", "Suspect", "Revenge", "Has no alibi", "Mislead")

    world.add_agent(alice, is_suspect=True)
    world.add_agent(bob, is_suspect=True)  # Add Bob as a suspect here
    world.add_agent(carol, is_suspect=True)

    # Simulate the world with agents acting over time
    for _ in range(3):  # Simulate 3 time units of world activity
        world.simulate_world()

    # Now let the player take actions to solve the mystery
    player_actions(world, storyteller)

def show_help():
    print("Mystery Game Help:")
    print("-run: Start the game simulation.")
    print("-help: Display help information.")
    print("-agents: List all agents in the game.")
    print("-time: Display the current game time.")
    print("-simulate <units>: Simulate world for specified time units.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1 or sys.argv[1] == "-help":
        show_help()
    elif sys.argv[1] == "-run":
        run_game()
    else:
        print("Unknown command. Use -help for available options.")