# storyteller.py

class Storyteller:
    def __init__(self, correct_suspect="Carol"):
        self.notebook = []
        self.timeline = []
        self.suspects_crossed_off = []
        self.clues_given = set()  # Track clues already given
        self.correct_suspect = correct_suspect  # The correct suspect

    def cross_off_suspect(self, suspect):
        if suspect not in self.suspects_crossed_off:
            self.suspects_crossed_off.append(suspect)
            print(f"Suspect crossed off: {suspect}")
        else:
            print(f"{suspect} has already been crossed off.")

    def reveal_final_suspect(self, world):
        """
        Reveals the final suspect if all others are crossed off or allows the player to guess.
        """
        remaining_suspects = [s for s in world.suspects if s not in self.suspects_crossed_off]
        
        if len(remaining_suspects) == 1:
            final_suspect = remaining_suspects[0]
            print(f"The final suspect is: {final_suspect}")
            
            # Check if the player's final suspect is the correct one
            if final_suspect == self.correct_suspect:
                print(f"Congratulations! You solved the crime. {final_suspect} is the culprit.")
            else:
                print(f"Sorry, you were wrong. The correct suspect was {self.correct_suspect}.")
        elif len(remaining_suspects) > 1:
            print(f"You still have {len(remaining_suspects)} suspects remaining.")
            choice = input("Would you like to guess the culprit now? (yes/no): ").lower()
            
            if choice == "yes":
                self.guess_culprit(remaining_suspects)
            else:
                print("Investigate further before making a guess.")
        else:
            print("No suspects remaining to solve the crime.")

    def guess_culprit(self, remaining_suspects):
        """
        Allows the player to guess the culprit from the remaining suspects.
        """
        print("\nWho do you think the culprit is?")
        for idx, suspect in enumerate(remaining_suspects):
            print(f"{idx + 1}. {suspect}")
        
        choice = int(input("Choose the suspect by number: ")) - 1
        if 0 <= choice < len(remaining_suspects):
            guessed_suspect = remaining_suspects[choice]
            print(f"You guessed: {guessed_suspect}")
            
            # Check if the guess is correct
            if guessed_suspect == self.correct_suspect:
                print(f"Congratulations! {guessed_suspect} is the culprit.")
            else:
                print(f"Sorry, {guessed_suspect} is not the culprit. The correct suspect was {self.correct_suspect}.")
        else:
            print("Invalid choice.")
            
    def update_timeline(self, event, time):
        """
        Add an event to the timeline and display it.
        """
        self.timeline.append((event, time))  # Track events with time
        print(f"Timeline Updated: {event} at time {time}")

    # Add clue to notebook logic
    def add_clue_to_notebook(self, clue, questionable=False):
        if clue not in self.clues_given:  # Only add the clue if it's not already given
            entry = {"clue": clue, "questionable": questionable}
            self.notebook.append(entry)
            self.clues_given.add(clue)
        else:
            print("This clue has already been noted.")
        self.display_notebook()

    def display_notebook(self):
        confirmed_clues = [entry['clue'] for entry in self.notebook if not entry['questionable']]
        questionable_clues = [entry['clue'] for entry in self.notebook if entry['questionable']]

        print("\n--- Notebook ---")
        print("\nConfirmed Clues:")
        for clue in confirmed_clues:
            print(f"  - {clue}")
        print("\nQuestionable Clues:")
        for clue in questionable_clues:
            print(f"  - {clue} (Questionable)")

        if self.suspects_crossed_off:
            print("\nCrossed-off Suspects:")
            for suspect in self.suspects_crossed_off:
                print(f"  - {suspect}")
        else:
            print("\nNo suspects have been crossed off yet.")
        print("----------------\n")

    # Other Storyteller methods like cross_off_suspect() and reveal_final_suspect()...