# game_world.py

class World:
    def __init__(self, storyteller, locations, world_time):
        self.storyteller = storyteller
        self.locations = locations
        self.agents = []
        self.suspects = []  # This list contains suspects to be crossed off
        self.world_time = world_time

    def add_agent(self, agent, is_suspect=False):
        """
        Add an agent to the world and, if applicable, add them to the suspects list.
        """
        self.agents.append(agent)
        if is_suspect:
            self.suspects.append(agent.name)  # Add agent's name to suspects if they're a suspect

    def update_story(self, event):
        """
        Updates the storyteller with a new event for the timeline.
        """
        self.storyteller.update_timeline(event, self.world_time.current_time)

    def simulate_world(self):
        """
        Simulate the world and make the agents act based on the progression of time.
        This method progresses time and lets each agent act accordingly.
        """
        # Advance time
        self.world_time.advance_time(1)
        
        # Let each agent act based on the current time
        for agent in self.agents:
            agent.act(self, self.world_time)