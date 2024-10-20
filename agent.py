import random

class Agent:
    def __init__(self, name, role, motive, alibi, goal):
        self.name = name
        self.role = role  # e.g., Suspect, Witness, Criminal
        self.motive = motive
        self.alibi = alibi
        self.goal = goal  # e.g., Mislead, Help, Neutral
        self.timeline = []
        self.clue_planted = False
        self.clues_given = set()  # Track clues already given

    def act(self, world, world_time):
        """
        The agent will act passively over time, planting clues or interacting with the environment.
        """
        if self.goal == 'Mislead':
            self.plant_clue(world, world_time)
        elif self.goal == 'Help':
            self.provide_clue(world, world_time)
        elif self.goal == 'Neutral':
            self.move_randomly(world, world_time)

    def plant_clue(self, world, world_time):
        """
        Adds deeper clues or more context instead of repeating the same basic information.
        """
        if not self.clue_planted:
            fake_clue = f"Fake letter implicating {random.choice(world.suspects)} at time {world_time.current_time}"
            if fake_clue not in self.clues_given:
                world.update_story(fake_clue)
                world.storyteller.add_clue_to_notebook(fake_clue, questionable=True)
                self.clue_planted = True
                self.clues_given.add(fake_clue)
        else:
            # Add new layers of the clue, such as additional context
            further_clue = f"{self.name} was seen holding something unusual near the crime scene."
            if further_clue not in self.clues_given:
                world.update_story(further_clue)
                world.storyteller.add_clue_to_notebook(further_clue)
                self.clues_given.add(further_clue)

    def provide_clue(self, world, world_time):
        """
        Provides helpful clues when the agent's goal is to help the player.
        """
        if "helpful_clue_given" not in self.clues_given:
            true_clue = f"{self.name} saw {random.choice(world.suspects)} near the scene at time {world_time.current_time}"
            if true_clue not in self.clues_given:
                world.update_story(true_clue)
                world.storyteller.add_clue_to_notebook(true_clue)
                self.clues_given.add("helpful_clue_given")
        else:
            # Provide deeper insight after the first clue
            deeper_clue = f"{self.name}: I remember seeing {random.choice(world.suspects)} carrying something suspicious."
            if deeper_clue not in self.clues_given:
                world.update_story(deeper_clue)
                world.storyteller.add_clue_to_notebook(deeper_clue)
                self.clues_given.add(deeper_clue)

    def move_randomly(self, world, world_time):
        """
        Neutral agents just move randomly without contributing clues.
        """
        location = random.choice(world.locations)
        self.timeline.append(f"{self.name} was at {location} at time {world_time.current_time}")
        print(f"{self.name} moved to {location} at time {world_time.current_time}")