import random
import game_world as world

# dialogue.py

class Dialogue:
    def __init__(self, agent, player, world):
        self.agent = agent
        self.player = player
        self.world = world  # Store world reference to access suspects

    def initiate(self):
        """
        The player can ask different questions and get more in-depth responses each time.
        """
        print(f"\n--- {self.agent.name}'s Dialogue ---")
        print("1. Ask about their alibi")
        print("2. Ask about their motive")
        print("3. Ask if they saw anything suspicious")

        question_choice = input("Choose a question (1-3): ")

        if question_choice == "1":
            return self.ask_about_alibi()
        elif question_choice == "2":
            return self.ask_about_motive()
        elif question_choice == "3":
            return self.ask_about_witness_info()
        else:
            print("Invalid choice.")
            return None

    def ask_about_alibi(self):
        """
        Provides more detailed alibi information.
        """
        if self.agent.alibi:
            alibi_info = f"{self.agent.name}: I was {self.agent.alibi} during the crime."
        else:
            alibi_info = f"{self.agent.name}: I have no alibi."
        print(alibi_info)
        return alibi_info

    def ask_about_motive(self):
        """
        Asks the agent about their motive.
        """
        if self.agent.motive:
            motive_info = f"{self.agent.name}: My motive? People say it's {self.agent.motive}, but I had no reason to commit a crime."
        else:
            motive_info = f"{self.agent.name}: I have no real motive."
        print(motive_info)
        return motive_info

    def ask_about_witness_info(self):
        """
        Provides more detailed information about what the suspect saw.
        """
        other_suspects = [s for s in self.world.suspects if s != self.agent.name]
        if other_suspects:
            witness_info = f"{self.agent.name}: I saw {random.choice(other_suspects)} acting suspiciously near the crime scene."
        else:
            witness_info = f"{self.agent.name}: I didn't see anything suspicious."
        print(witness_info)
        return witness_info